import os
import pickle

def predict_email(model_file, vectorizer_file, email_text):
    try:
        # Check if files exist
        if not os.path.exists(model_file):
            raise FileNotFoundError(f"Model file not found: {model_file}")
        if not os.path.exists(vectorizer_file):
            raise FileNotFoundError(f"Vectorizer file not found: {vectorizer_file}")

        # Load the model
        with open(model_file, "rb") as f:
            model = pickle.load(f)
        
        # Load the vectorizer
        with open(vectorizer_file, "rb") as f:
            vectorizer_data = pickle.load(f)
            # Check if the loaded data is a tuple
            if isinstance(vectorizer_data, tuple) and len(vectorizer_data) >= 3:
                vectorizer = vectorizer_data[2]
            else:
                raise ValueError("The vectorizer file format is invalid.")

        # Vectorize the input email
        email_vector = vectorizer.transform([email_text])

        # Make a prediction
        prediction = model.predict(email_vector)
        return "Phishing" if prediction[0] == 1 else "Not Phishing"
    except Exception as e:
        raise RuntimeError(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    print("Welcome to the Phishing Email Detection Program!")
    email_text = input("Enter the email text to analyze: ")

    # Dynamic paths
    model_file = os.path.join("models", "phishing_detector.pkl")
    vectorizer_file = os.path.join("data", "preprocessed_data.pkl")

    try:
        result = predict_email(model_file, vectorizer_file, email_text)
        print(f"The email is classified as: {result}")
    except Exception as e:
        print(f"Error: {e}")
