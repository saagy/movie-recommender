import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st

movies = pd.read_csv('movies.csv')

def clean_title(title):
    return re.sub(r'[^a-zA-Z0-9 ]', '', title)

movies['cleaned_title'] = movies['title'].apply(clean_title)

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(movies['cleaned_title'])
 
def search(title):
    title = clean_title(title)
    title_vec = vectorizer.transform([title])
    cosine_similarities = cosine_similarity(title_vec, tfidf_matrix).flatten()
    #related_movie_indices = cosine_similarities.argsort()[-10:][::-1]
    #return movies.iloc[related_movie_indices][['title', 'year', 'genre']]
    indices = np.argpartition(cosine_similarities, -5)[-5:]
    results = movies.iloc[indices][::-1]
    return results

ratings = pd.read_csv('ratings.csv')
def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[similar_user_recs > .10]

    all_users = ratings[(ratings['movieId'].isin(similar_user_recs.index)) & (ratings['rating'] > 4)]
    all_user_recs = all_users['movieId'].value_counts() / len(all_users['userId'].unique())

    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ['similar', 'all']
    rec_percentages['score'] = rec_percentages['similar'] / rec_percentages['all']
    rec_percentages = rec_percentages.sort_values('score', ascending=False)
    rec_percentages = rec_percentages.merge(movies, left_index=True, right_on='movieId')
    return rec_percentages[rec_percentages['movieId'] != movie_id].head(10)[['title', 'score']]


st.title("Movie Suggestion App")
title = st.text_input("Enter a movie title:")
if len(title) > 5:
    results = search(title)
    movie_id = results.iloc[0]['movieId']
    st.write("Top search results:")
    st.write(find_similar_movies(movie_id))

