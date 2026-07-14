# Sentiment Analysis of Comments Received Through E-Consultation Modules Using Machine Learning

# 🩺 AI Medical Sentiment Analysis System

## 📖 Project Overview

The **AI Medical Sentiment Analysis System** is a Flask-based web application built with **Python** and **MySQL**. It analyzes patient feedback from an E-Consultation system and classifies it as **Positive** or **Negative** using NLP and Machine Learning.

It also includes a secure **Admin Dashboard** to view submitted feedback and sentiment statistics.

---

## 🚀 Features

### User Module

* Submit medical feedback
* AI-based sentiment prediction
* Instant result display
* Input validation

### Admin Module

* Secure admin login
* Protected dashboard
* View submitted feedback
* View sentiment counts
* Logout functionality

---

## 🛠 Technologies Used

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Pickle

### Frontend

* HTML5
* CSS3

### Database

* MySQL

---

## 📂 Project Structure

```text
SentimentAnalysisProject/

│── app.py
│── db.py
│── train_model.py
│── test_model.py
│── model.pkl
│── vectorizer.pkl
│── dataset.csv
│── requirements.txt
│── README.md

├── templates/
│   ├── index.html
│   ├── login.html
│   └── dashboard.html

├── static/
│   └── style.css

└── venv/
```

---

## ⚙️ Installation

1. Clone the repository.

2. Activate the virtual environment.

```bash
venv\Scripts\activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Configure the MySQL database.

5. Run the application.

```bash
python app.py
```

6. Open in your browser.

```
http://127.0.0.1:5000
```

---

## 🧪 Testing

The application was tested for:

* Empty and whitespace input
* Positive and negative feedback
* Numbers-only and special character input
* Emoji handling
* SQL Injection and XSS attempts
* Admin authentication and dashboard protection

---

## 📈 Future Enhancements

* Neutral sentiment prediction
* Sentiment graphs and charts
* Email notifications
* Export reports to PDF or Excel
* Cloud deployment

---

## 👨‍💻 Developed By

**Nikita Pradhan**

B.Sc. Computer Science

Ravenshaw University
