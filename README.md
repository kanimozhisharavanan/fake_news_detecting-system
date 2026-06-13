# Fake News Detection System

## Overview
The Fake News Detection System is a machine learning-based web application that classifies news articles as Real or Fake. The system uses Natural Language Processing (NLP) techniques and a Logistic Regression model to analyze news text and predict its authenticity.

## Features
- User login authentication
- Fake/Real news prediction
- Machine Learning model using Logistic Regression
- Interactive web interface using Flask
- Statistics dashboard showing prediction counts
- Graphical visualization using Chart.js

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- HTML
- JavaScript
- Chart.js
- Pickle

## Project Structure

fake_news_detecting-system/
│
├── web_app.py
├── train.py
├── fake_news_model.pkl
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── login.html
│   └── index.html
│
└── data/
    └── news.csv

## Installation

1. Clone the repository

git clone https://github.com/kanimozhisharavanan/fake_news_detecting-system.git

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python web_app.py

4. Open browser

http://127.0.0.1:5000

## Login Credentials

Username: admin

Password: 1234

## Working

1. User logs into the system.
2. News text is entered into the input field.
3. The trained machine learning model processes the text.
4. The system predicts whether the news is Real or Fake.
5. Results and statistics are displayed on the dashboard.

## Future Enhancements

- Larger dataset for improved accuracy
- Deep Learning models
- News API integration
- User management system
- Real-time fact checking

## Author

Kanimozhi S
