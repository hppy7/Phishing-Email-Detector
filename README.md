
# Phishing Email Detector

The Phishing Email Detector is a machine learning project that utilizes Natural Language Processing (NLP) techniques to identify and classify phishing emails. The goal of this project is to help users recognize potentially harmful emails and protect themselves from phishing attacks.<br> Author Sundhir Singh

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup and Usage](#setup-and-usage)
  - [Step 1: Install Dependencies](#step-1-install-dependencies)
  - [Step 2: Preprocess Data](#step-2-preprocess-data)
  - [Step 3: Train the Model](#step-3-train-the-model)
  - [Step 4: Make Predictions](#step-4-make-predictions)
- [How It Works](#how-it-works)


---

## Overview
The Phishing Email Detector employs various machine learning algorithms to classify emails as phishing or legitimate. By preprocessing email data and extracting relevant features, the model can effectively identify potentially harmful emails.

## Features
- Preprocessing of email data to extract relevant features.
- Implementation of various machine learning algorithms for classification.
- Evaluation of model performance using metrics such as accuracy, precision, and recall.
- User-friendly interface for making predictions on new emails.

## **Technologies Used**
- **Python**: Programming language.
- **Scikit-learn**: Library for machine learning algorithms.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Library for numerical computing.
- **Flask** (optional): Can be used to deploy the model as a web service.
- **Pickle**: For saving and loading the trained model.



## Installation
To run this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phishing-email-detector.git
   cd phishing-email-detector
Install the required packages:




Preprocess the Data: Run the preprocessing script to clean and prepare the email dataset.
python preprocess.py
Train the Model: Train the machine learning model using the preprocessed data.
python train.py
Make Predictions: Use the trained model to predict whether a new email is phishing or not.
## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/phishing-email-detection.git
cd phishing-email-detection


### **2. Set up a Virtual Environment (optional but recommended)**
```bash
python -m venv venv
```
Activate the virtual environment:
- **Windows**: 
  ```bash
  venv\bin
  cd venv\bin
  .\Activate or .\Activate.ps1 # For Windows u need to enter that in powershell 
  ```
- **macOS/Linux**: 
  ```bash
  source venv/bin/activate
  ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Setup and Usage**

### **Step 1: Install Dependencies**
Make sure all required libraries are installed:
```bash
pip install -r requirements.txt
```

### **Step 2: Preprocess Data**
Run the `preprocess.py` script to preprocess the raw data and save it as a pickle file:
```bash
python src/preprocess.py
```
This script:
- Loads the raw email dataset (`phishing_emails.csv`).
- Converts the email text into a numerical format using TF-IDF vectorization.
- Saves the processed data to `preprocessed_data.pkl`.

### **Step 3: Train the Model**
Train the machine learning model by running the `train.py` script:
```bash
python src/train.py
```
This script:
- Loads the preprocessed data.
- Splits it into training and testing sets.
- Trains a Random Forest classifier (or other ML models) using the training data.
- Saves the trained model to `phishing_detector.pkl`.

**Note**: To try a different model, replace the `RandomForestClassifier` in `train.py` with another algorithm, like `LogisticRegression`.

### **Step 4: Make Predictions**
Predict phishing emails using the `predict.py` script:
```bash
python src/predict.py
```
This script:
- Loads the trained model (`phishing_detector.pkl`) and vectorizer.
- Takes an input email and predicts whether it’s phishing or legitimate.

To test with your own email, modify the `email_text` variable in `predict.py`:
```python
email_text = "Your account has been compromised. Click here to reset your password."
```

---
## **How It Works**

### **1. Preprocessing**
- Converts raw email content into numerical feature vectors using TF-IDF vectorization. This calculates the importance of each word in the email relative to other emails.

### **2. Model Training**
- Trains a Random Forest model to classify emails as phishing or not based on text patterns.

### **3. Prediction**
- For a new email, the model predicts whether it is phishing or legitimate using the patterns it learned during training.

---

## **Troubleshooting Virtual Environment**
If the virtual environment becomes "locked" (you cannot install or uninstall packages), it may be due to a corrupted `pip` cache. To fix this:
1. Deactivate the virtual environment:
   ```bash
   deactivate
   ```
2. Remove the `venv` folder:
   ```bash
   rm -rf venv
   ```
3. Recreate and activate the virtual environment:
   ```bash
   python -m venv venv
   cd venv\bin
   \Activate or .\Activate.ps1 # For Windows u need to enter that in powershell 
   source venv/bin/activate  # For macOS/Linux
   ```
4. Reinstall dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---










Acknowledgments
Sundhir Singh - for the initial idea and implementation.
This project aims to detect whether an email is phishing or not, helping users stay safe from potential threats.
Feel free to modify any part of the text to better suit your project or personal style!



