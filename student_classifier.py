import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class StudentClassifier:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)

    def prepare_data(self):
        X = self.data[
            ["StudyHours", "Attendance", "PreviousMarks", "Assignments"]
        ]

        y = self.data["Result"].map({
            "Fail": 0,
            "Pass": 1
        })

        return X, y

    def train_model(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model = LogisticRegression()

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\n===== MODEL TRAINED =====")
        print("Logistic Regression model trained successfully. ✅")

        print("\n===== MODEL EVALUATION =====")
        print(f"Accuracy: {accuracy * 100:.2f}%")

    def predict_result(self, study_hours, attendance, previous_marks, assignments):

        new_student = pd.DataFrame({
            "StudyHours": [study_hours],
            "Attendance": [attendance],
            "PreviousMarks": [previous_marks],
            "Assignments": [assignments]
        })

        prediction = self.model.predict(new_student)

        result = "PASS" if prediction[0] == 1 else "FAIL"

        print("\n===== STUDENT RESULT PREDICTION =====")
        print(f"Study Hours    : {study_hours}")
        print(f"Attendance     : {attendance}%")
        print(f"Previous Marks : {previous_marks}")
        print(f"Assignments    : {assignments}")
        print(f"Predicted Result: {result}")