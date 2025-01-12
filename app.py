from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model and vectorizer
MODEL_FILE = r"models/phishing_detector.pkl"
VECTORIZER_FILE = r"data/preprocessed_data.pkl"

with open(MODEL_FILE, "rb") as model_file:
    model = pickle.load(model_file)

with open(VECTORIZER_FILE, "rb") as vectorizer_file:
    _, _, vectorizer = pickle.load(vectorizer_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form["email_text"]
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)
    result = "Phishing" if prediction[0] == 1 else "Not Phishing"
    return render_template("index.html", result=result, email_text=email_text)

if __name__ == "__main__":
    app.run(debug=True)
