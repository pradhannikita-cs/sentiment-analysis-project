import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


comments = [
    "The doctor was very helpful",
    "I am not satisfied with the doctor",
    "The consultation was terrible",
    "The doctor explained everything clearly"
    "This is the worst service ever."
]


for comment in comments:
    data = vectorizer.transform([comment])
    result = model.predict(data)[0]
    print(comment, "---->", result)