from student_classifier import StudentClassifier


classifier = StudentClassifier("students.csv")

classifier.train_model()

print("\n===== ENTER NEW STUDENT DETAILS =====")

study_hours = float(input("Study hours: "))
attendance = float(input("Attendance (%): "))
previous_marks = float(input("Previous marks: "))
assignments = int(input("Assignments completed: "))

classifier.predict_result(
    study_hours,
    attendance,
    previous_marks,
    assignments
)