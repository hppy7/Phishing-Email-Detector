import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def preprocess_data(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # Load the CSV file
    data = pd.read_csv(input_file)

    # Ensure the dataset has 'text' and 'label' columns
    if 'text' not in data.columns or 'label' not in data.columns:
        raise ValueError("Input CSV must have 'text' and 'label' columns.")

    # Check for empty or missing data
    data.dropna(subset=['text', 'label'], inplace=True)

    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['text']).toarray()

    # Extract labels
    y = data['label'].values

    # Save preprocessed data and vectorizer
    with open(output_file, "wb") as f:
        pickle.dump((X, y, vectorizer), f)

    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    # Example usage with paths
    input_file = os.path.join("data", "phishing_emails.csv")
    output_file = os.path.join("data", "preprocessed_data.pkl")

    try:
        preprocess_data(input_file, output_file)
    except Exception as e:
        print(f"Error: {e}")
