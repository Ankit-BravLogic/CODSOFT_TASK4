# 🛡️ SpamShield AI

### AI-Powered SMS Spam Detection

SpamShield AI is a Machine Learning application that classifies SMS messages as **Spam** or **Legitimate (Ham)** using Natural Language Processing and Multinomial Naive Bayes.

The project was developed as part of the **CodSoft Machine Learning Internship — Task 4: Spam SMS Detection**.

---

## 🚀 Project Overview

Spam messages are unwanted messages that may contain advertisements, scams, fraudulent offers, or suspicious links.

SpamShield AI uses Machine Learning to automatically analyze the text of an SMS and predict whether it is:

- 🟢 **HAM** — Legitimate message
- 🔴 **SPAM** — Unwanted or suspicious message

The project includes an interactive Streamlit web application where users can enter an SMS and receive an instant prediction.

---

## ✨ Features

- 📱 SMS spam detection
- 🤖 Machine Learning classification
- 🧠 TF-IDF text feature extraction
- 📊 Multinomial Naive Bayes classifier
- 📈 Model probability display
- 💬 Interactive Streamlit interface
- 🔢 Message character and word counter
- 💡 Example messages for quick testing
- 🧠 Explanation of the ML pipeline
- 📱 Responsive web interface

---

## 🧠 Machine Learning Workflow

The project follows this workflow:

```text
SMS Message
     ↓
Text Preprocessing
     ↓
Train/Test Split
     ↓
TF-IDF Vectorization
     ↓
Multinomial Naive Bayes
     ↓
Prediction
     ↓
HAM / SPAM
```

---

## 📊 Dataset

The project uses the **SMS Spam Collection** dataset.

The dataset contains:

- **5,572 SMS messages**
- **4,825 Ham messages**
- **747 Spam messages**

### Class Distribution

| Label | Messages | Percentage |
|---|---:|---:|
| Ham | 4,825 | 86.59% |
| Spam | 747 | 13.41% |
| **Total** | **5,572** | **100%** |

Because the dataset is imbalanced, evaluation uses metrics such as:

- Precision
- Recall
- F1-score
- Confusion Matrix

rather than relying only on accuracy.

---

## 🔤 Text Representation — TF-IDF

Machine Learning algorithms cannot directly understand raw text.

Therefore, SMS messages are converted into numerical features using:

**TF-IDF — Term Frequency-Inverse Document Frequency**

The vectorizer was fitted only on the training data and then used to transform the test data.

This helps prevent data leakage between training and testing datasets.

---

## 🤖 Machine Learning Model

### Multinomial Naive Bayes

The primary model used in this project is:

```text
MultinomialNB
```

Naive Bayes is well suited for text classification problems because it works effectively with word-frequency-based features such as TF-IDF.

---

## 🔬 Model Evaluation

The dataset was divided into:

- **Training data: 80%**
- **Testing data: 20%**

The split used stratification to preserve the Spam/Ham class distribution.

### Naive Bayes Performance

**Accuracy: 96.86%**

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Ham | 0.97 | 1.00 | 0.98 |
| Spam | 1.00 | 0.77 | 0.87 |

### Confusion Matrix

```text
                 Predicted
              Ham       Spam

Actual Ham    966        0
Actual Spam    35       114
```

This means:

- 966 legitimate messages were correctly classified.
- 114 spam messages were correctly detected.
- 35 spam messages were incorrectly classified as legitimate.
- 0 legitimate messages were incorrectly classified as spam.

---

## 🔍 Model Comparison

A Logistic Regression model was also tested.

| Model | Spam Recall | Spam F1 |
|---|---:|---:|
| Multinomial Naive Bayes | 0.77 | 0.87 |
| Logistic Regression | 0.76 | 0.86 |

Based on this test split, **Multinomial Naive Bayes** was selected as the final model because it achieved slightly better Spam recall and F1-score.

---

## 🖥️ Streamlit Application

The project includes an interactive web interface built using Streamlit.

Users can:

1. Enter an SMS message.
2. Analyze the message.
3. Receive a HAM/SPAM prediction.
4. View the model's predicted probability.
5. See message statistics.
6. Try example messages.
7. Learn how the ML model works.

---

## 📂 Project Structure

```text
CODSOFT_TASK4/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── spam.csv
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── spam_detection.ipynb
│
└── src/
```

---

## ⚙️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Multinomial Naive Bayes
- Logistic Regression

### Natural Language Processing

- TF-IDF Vectorization

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Web Application

- Streamlit

### Model Persistence

- Joblib

### Development

- Jupyter Notebook
- VS Code
- Git & GitHub

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd CODSOFT_TASK4
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

**macOS/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\\Scripts\\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Example Predictions

### Legitimate Message

```text
Hey, are you coming to class today?
```

**Prediction: HAM**

### Spam Message

```text
Congratulations! You have won a free prize.
Call now to claim your reward!
```

**Prediction: SPAM**

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how Natural Language Processing and Machine Learning can be used to automatically detect spam SMS messages.

This project also demonstrates the complete ML workflow:

```text
Data
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Model Evaluation
 ↓
Model Saving
 ↓
Web Application
 ↓
Deployment
```

---

## 🔮 Future Improvements

Possible future improvements include:

- Advanced text preprocessing
- Word embeddings
- Transformer-based NLP models
- Larger and more diverse datasets
- Improved probability calibration
- Multilingual SMS detection
- REST API integration
- Cloud deployment
- Real-time SMS integration

---

## 👨‍💻 Internship

This project was developed as part of the:

**CodSoft Machine Learning Internship**

### Task 4 — Spam SMS Detection

---

## 📜 Disclaimer

This application is an educational Machine Learning project.

Predictions should not be treated as a guaranteed determination that a message is malicious or safe.

---

## ⭐ Acknowledgement

Thanks to CodSoft for providing the Machine Learning internship opportunity and project-based learning experience.
