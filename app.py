from flask import Flask, render_template, request, redirect, url_for, session
import pickle
from db import get_connection

print(">>> APP.PY HAS STARTED <<<")

app = Flask(__name__)
app.secret_key = "secretkey"

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Database connection
db = get_connection()


# ---------------- HOME PAGE ---------------- #

@app.route("/", methods=["GET", "POST"])
def home():

    message = session.pop("message", None)
    prediction = session.pop("prediction", None)

    print("Prediction value:", prediction)

    return render_template(
        "index.html",
        message=message,
        prediction=prediction
    )

    

# ---------------- PREDICT FEEDBACK ---------------- #

@app.route("/predict", methods=["POST"])
def predict():

    # Get feedback from user
    comment = request.form["comment"]

    comment = comment.strip()

    if not comment:
     session["message"] = "⚠️ Please enter your feedback before submitting."
     return redirect(url_for("home"))
    
    # Check if the feedback contains at least one alphabet
    if not any(char.isalpha() for char in comment):
     session["message"] = "⚠️ Please enter meaningful feedback."
     return redirect(url_for("home"))

    # Convert text into numbers
    data = vectorizer.transform([comment])

    # Predict sentiment
    prediction = model.predict(data)[0]

    session["prediction"] = prediction

    print("Comment:", comment)
    print("Prediction:", prediction)

    # Save into database
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO feedback(comment, sentiment) VALUES(%s,%s)",
        (comment, prediction)
    )

    db.commit()

    print("Data saved successfully!")

    cursor.close()

    # Success message
    session["message"] = "✅ Thank you for your valuable feedback!"

    return redirect(url_for("home"))


@app.route("/login")
def login():

    return render_template("login.html")

@app.route("/admin_login", methods=["POST"])
def admin_login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":

        session["admin"] = True

        return redirect(url_for("dashboard"))

    return render_template(
        "login.html",
        error="Invalid username or password!"
    )

@app.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect(url_for("login"))

# ---------------- ADMIN DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if not session.get("admin"):
     return redirect(url_for("login"))

    cursor = db.cursor(dictionary=True)

    # Get all feedback
    cursor.execute("SELECT * FROM feedback ORDER BY id DESC")
    feedbacks = cursor.fetchall()

    # Total Feedback
    cursor.execute("SELECT COUNT(*) AS total FROM feedback")
    total = cursor.fetchone()["total"]

    # Positive Feedback
    cursor.execute("SELECT COUNT(*) AS positive FROM feedback WHERE sentiment='positive'")
    positive = cursor.fetchone()["positive"]

    # Negative Feedback
    cursor.execute("SELECT COUNT(*) AS negative FROM feedback WHERE sentiment='negative'")
    negative = cursor.fetchone()["negative"]

    # Neutral Feedback
    cursor.execute("SELECT COUNT(*) AS neutral FROM feedback WHERE sentiment='neutral'")
    neutral = cursor.fetchone()["neutral"]

    # Calculate percentages
    if total > 0:
        positive_percent = round((positive / total) * 100, 1)
        neutral_percent = round((neutral / total) * 100, 1)
        negative_percent = round((negative / total) * 100, 1)
    else:
        positive_percent = 0
        neutral_percent = 0
        negative_percent = 0

    cursor.close()

    return render_template(
        "dashboard.html",
        feedbacks=feedbacks,
        total=total,
        positive=positive,
        neutral=neutral,
        negative=negative,
        positive_percent=positive_percent,
        neutral_percent=neutral_percent,
        negative_percent=negative_percent
    )


# ---------------- RUN APPLICATION ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
