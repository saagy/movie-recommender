# 🎬 Movie Recommendation App

A simple movie recommender system built with:
- TF-IDF Vectorizer for title-based search
- Collaborative filtering using user ratings
- Streamlit for the web interface

## 🚀 Features
- Search for movies by title (fuzzy matching with TF-IDF)
- Get top similar movies based on what other users rated highly
- Interactive Streamlit UI

## 📂 Project Structure
movie-recommender/
│── app.py
│── movies.csv
│── ratings.csv
│── requirements.txt
│── README.md


## ▶️ How to Run
1. Clone this repository:
   git clone https://github.com/saagy/movie-recommender.git
   cd movie-recommender
   
2.Install dependencies:
pip install -r requirements.txt

3.Run the app:
streamlit run movieSuggest.py
