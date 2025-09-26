# 🎬 Movie Recommendation App

A simple **movie recommender system** built with Python and Streamlit.  
It combines:
- **TF-IDF Vectorizer** for title-based search
- **Collaborative filtering** using user ratings
- **Streamlit** for the interactive UI

---

## 🚀 Features
- Search for movies by title (supports partial/fuzzy matches)
- Get similar movies based on what other users rated highly
- Interactive and easy-to-use web interface

---

## 📂 Project Structure
movie-recommender/
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── README.md # Documentation
│── .gitignore # Ignore datasets, caches, etc.


---

## 📊 Dataset
This project uses the **MovieLens 25M dataset** provided by [GroupLens](https://grouplens.org/datasets/movielens/).  

Download the following files and place them in the project folder:
- [movies.csv](https://files.grouplens.org/datasets/movielens/ml-25m.zip)  
- [ratings.csv](https://files.grouplens.org/datasets/movielens/ml-25m.zip)  

👉 After downloading, extract the `ml-25m.zip` file and copy `movies.csv` and `ratings.csv` into your project directory.

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-recommender.git
   cd movie-recommender
2. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn streamlit
   
Add the dataset (movies.csv and ratings.csv) into the project folder.

3.Run the app:
streamlit run app.py
Open your browser → http://localhost:8501

🛠 Requirements
Python 3.8+

pandas

numpy

scikit-learn

streamlit

(Already included in requirements.txt)

📌 Notes
The dataset is not included in this repository due to size. Please download it manually as shown above.

You can extend this app by adding new recommendation algorithms or deploying it to Streamlit Cloud for live demos.
