from flask import Flask, render_template, request
import pickle
from db import get_connection

print(">>> APP.PY HAS STARTED <<<")

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


db = get_connection()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Get feedback from user
    comment = request.form["comment"]

    # Convert text into numbers
    data = vectorizer.transform([comment])

    # Predict sentiment
    prediction = model.predict(data)[0]

    print("Comment:", comment)
    print("Prediction:", prediction)

    # Save to database
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO feedback(comment, sentiment) VALUES(%s,%s)",
        (comment, prediction)
    )
    db.commit()
    cursor.close()

    return render_template(
    "index.html",
    prediction=prediction,
    message="Thank you for your valuable feedback!"
)



if __name__ == "__main__":
    app.run(debug=True)