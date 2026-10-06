# 🎓 Student Performance Classifier

A beginner-friendly Machine Learning project that predicts whether a student is likely to **Pass or Fail** using **Logistic Regression**.

The prediction is based on:

- Study Hours
- Attendance
- Previous Marks
- Assignments Completed

This project is part of my Python → Data Science → Machine Learning learning journey.

---

## 🚀 Project Overview

The **Student Performance Classifier** uses student academic information to classify the student's expected result as either:

```text
PASS
```

or

```text
FAIL
```

The project demonstrates a basic Machine Learning classification workflow:

```text
Student Dataset
       ↓
Feature Selection
       ↓
Target Encoding
       ↓
Train/Test Split
       ↓
Logistic Regression
       ↓
Model Training
       ↓
Accuracy Evaluation
       ↓
New Student Input
       ↓
PASS / FAIL Prediction
```

---

## 🎯 Objective

The main objective of this project is to understand the fundamentals of **Machine Learning Classification**.

The project helps demonstrate:

- Features and target variables
- Categorical target encoding
- Train/test splitting
- Logistic Regression
- Model training
- Classification prediction
- Accuracy evaluation
- Using a trained model for new data

---

## 🧠 Machine Learning Concepts

### 1. Features

The model uses four features:

```text
StudyHours
Attendance
PreviousMarks
Assignments
```

These features describe the student's academic performance.

In Machine Learning:

```text
X → Input Features
```

---

### 2. Target

The target column is:

```text
Result
```

It contains:

```text
Pass
Fail
```

Since Machine Learning models work with numerical values, the target is converted into:

```text
Fail → 0
Pass → 1
```

This allows the classification model to learn from the target values.

---

## 📊 Dataset

The project uses a sample dataset containing 30 student records.

Example:

```csv
Name,StudyHours,Attendance,PreviousMarks,Assignments,Result
Rahul,2,55,38,3,Fail
Aman,3,60,42,4,Fail
Priya,5,75,58,7,Pass
Neha,6,80,65,8,Pass
Arjun,7,85,72,9,Pass
```

The dataset is designed for learning and demonstration purposes.

---

## 🤖 Logistic Regression

This project uses:

```python
LogisticRegression()
```

Logistic Regression is commonly used for **classification problems**.

Instead of predicting a continuous numerical value, the model predicts a class.

For this project:

```text
Student Information
       ↓
Logistic Regression
       ↓
PASS / FAIL
```

---

## 🔀 Train/Test Split

The dataset is divided into:

```text
80% → Training Data
20% → Testing Data
```

The training data is used to teach the model.

The testing data is used to evaluate the model on data that was not used during training.

The project uses:

```python
random_state=42
```

This makes the random split reproducible.

---

## 📈 Model Evaluation

The project uses **Accuracy** to evaluate the classifier.

Accuracy represents the percentage of predictions that were correct.

For example:

```text
Accuracy = 90%
```

means that the model correctly classified approximately 90% of the tested samples.

### Important Note

The dataset contains only 30 records, so a very high accuracy score does **not** mean that this model is ready for real-world student assessment.

The project is primarily intended to learn Machine Learning classification concepts.

---

## 🧪 Example Prediction

The program asks the user for new student information:

```text
===== ENTER NEW STUDENT DETAILS =====

Study hours: 7
Attendance (%): 85
Previous marks: 75
Assignments completed: 9
```

The trained model then predicts:

```text
===== STUDENT RESULT PREDICTION =====

Study Hours    : 7.0
Attendance     : 85.0%
Previous Marks : 75.0
Assignments    : 9
Predicted Result: PASS
```

---

## 🗂️ Project Structure

```text
python-student-performance-classifier/
│
├── main.py
├── student_classifier.py
├── students.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsible for:

- Creating the classifier
- Training the model
- Taking new student information
- Sending the information to the prediction method

### `student_classifier.py`

Contains the Machine Learning logic:

- Loading the dataset
- Preparing features
- Encoding the target
- Splitting the dataset
- Training Logistic Regression
- Evaluating accuracy
- Predicting a new student's result

### `students.csv`

Contains the student training dataset.

### `requirements.txt`

Contains the Python libraries required by the project.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ayushman-ece/python-student-performance-classifier.git
```

Move into the project directory:

```bash
cd python-student-performance-classifier
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Run:

```bash
python main.py
```

The program will train the model and display its accuracy.

It will then ask for a new student's information.

Example:

```text
Study hours: 7
Attendance (%): 85
Previous marks: 75
Assignments completed: 9
```

The program will return:

```text
Predicted Result: PASS
```

---

## 🧰 Technologies Used

- Python
- Pandas
- Scikit-learn
- Logistic Regression
- Machine Learning
- Classification
- CSV

---

## 📦 Requirements

The project requires:

```text
pandas
scikit-learn
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📚 What I Learned

Through this project, I learned:

1. The difference between regression and classification
2. What features and targets are
3. How to encode categorical target values
4. How to split data into training and testing sets
5. How Logistic Regression can be used for classification
6. How to train a classification model
7. How to make predictions
8. How to evaluate a classifier using accuracy
9. How to use a trained model with new input data
10. How to build a basic end-to-end Machine Learning application

---

## 🔄 Regression vs Classification

This project follows my previous Employee Salary Predictor project.

### Regression

Previous project:

```text
Employee Information
        ↓
Linear Regression
        ↓
Salary: ₹65,000
```

Regression predicts a numerical value.

### Classification

Current project:

```text
Student Information
        ↓
Logistic Regression
        ↓
PASS / FAIL
```

Classification predicts a category.

---

## ⚠️ Limitations

This project uses a small sample dataset.

Therefore:

- The dataset is not large enough for reliable real-world predictions.
- Accuracy can vary significantly with different train/test splits.
- Student performance depends on many factors not included in the dataset.
- The current model only predicts two classes: Pass and Fail.
- Input validation is basic.

This project should be considered an **educational Machine Learning project**, not a real student evaluation system.

---

## 🔮 Future Improvements

Possible improvements include:

- Add a much larger dataset
- Add more student features
- Add study consistency
- Add previous semester performance
- Add assignment quality
- Add sleep hours
- Add extracurricular activity
- Add confusion matrix
- Add precision, recall, and F1-score
- Compare multiple classification algorithms
- Add Random Forest Classifier
- Add Decision Tree Classifier
- Add a graphical user interface
- Build a Streamlit web application
- Deploy the model as an API

---

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece

---

## 🛣️ Learning Journey

This project is part of my long-term journey:

```text
Python
   ↓
Data Analysis
   ↓
Data Science
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
LLMs
   ↓
RAG
   ↓
Agentic AI
```

The goal is to build practical projects while understanding the concepts behind them step-by-step.