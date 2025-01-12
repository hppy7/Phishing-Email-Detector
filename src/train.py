import os
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data_file, model_file):
    try:
        # Check if the data file exists
        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Data file not found: {data_file}")

        # Load preprocessed data
        print(f"Loading preprocessed data from {data_file}...")
        with open(data_file, "rb") as f:
            X, y, _ = pickle.load(f)

        # Check if the data is loaded properly
        if X is None or y is None:
            raise ValueError("The data or labels could not be loaded properly.")

        # Split data into training and testing sets
        print("Splitting data into training and testing sets...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest model
        print("Training the Random Forest model...")
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        print("Evaluating the model...")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        # Save the trained model
        print(f"Saving the model to {model_file}...")
        with open(model_file, "wb") as f:
            pickle.dump(model, f)

        print("Model training and saving complete.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    data_file = os.path.join("data", "preprocessed_data.pkl")
    model_file = os.path.join("models", "phishing_detector.pkl")

    try:
        train_model(data_file, model_file)
    except Exception as e:
        print(f"Error: {e}")
