from flask import Flask, render_template, request, redirect, session
import pickle

app = Flask(__name__)
app.secret_key = "secret123"

# Load model
with open("model/fake_news_model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

# Count storage
real_count = 0
fake_count = 0

def predict_news(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    return "Real" if prediction == 1 else "Fake"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == "admin" and pwd == "1234":
            session["user"] = user
            return redirect("/home")
        else:
            return "Invalid Login ❌"
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    global real_count, fake_count

    if "user" not in session:
        return redirect("/")

    result = ""
    color = ""

    if request.method == "POST":
        news = request.form["news"]
        result = predict_news(news)

        if result == "Real":
            real_count += 1
            color = "green"
        else:
            fake_count += 1
            color = "red"

    return render_template("index.html",
                           result=result,
                           color=color,
                           real=real_count,
                           fake=fake_count)

if __name__ == "__main__":
    app.run(debug=True)