# Sentiment Analysis Web Application

## Project Overview

This project is a Machine Learning based web application that analyzes user comments and predicts whether the sentiment is Positive, Negative, or Neutral.

The application uses Natural Language Processing (NLP) and Machine Learning techniques for sentiment classification.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

## Features

- User enters a comment
- ML model analyzes the text
- Predicts sentiment
- Displays the result on webpage

## Project Structure
SentimentAnalysisProject/

│── app.py
│── train_model.py
│── test_model.py
│── dataset.csv
│── model.pkl
│── vectorizer.pkl

├── templates/
│      └── index.html

└── static/
       └── style.css

## How to Run


1. Activate virtual environment

venv\Scripts\activate

2. Run Flask application

python app.py

3. Open browser:

http://127.0.0.1:5000