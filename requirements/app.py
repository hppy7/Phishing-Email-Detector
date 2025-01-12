from flask import Flask, request, render_template
import pickle
import os

# Initialize Flask app
app = Flask(__name__)

# Define the paths for model and vectorizer
MODEL_PATH = "models/phishing_detector.pkl"
VECTORIZER_PATH = "data/preprocessed_data.pkl"

# Ensure the paths exist before loading the model
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError(f"Model or vectorizer file not found at specified paths: {MODEL_PATH}, {VECTORIZER_PATH}")

# Load the trained model and vectorizer
with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

with open(VECTORIZER_PATH, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form["email_text"]
    
    # Transform the input text
    email_vector = vectorizer.transform([email_text])
    
    # Get the prediction (1: phishing, 0: not phishing)
    prediction = model.predict(email_vector)[0]
    
    # Convert prediction to result
    result = "Phishing" if prediction == 1 else "Not Phishing"
    
    # Return the result and the email text to the template
    return render_template("index.html", prediction=result, email=email_text)

if __name__ == "__main__":
    app.run(debug=True)
