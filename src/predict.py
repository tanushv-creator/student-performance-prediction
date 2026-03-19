import joblib
import pandas as pd

# Load saved model
model = joblib.load("models/best_model.pkl")

# Sample student data
# [studytime, failures, absences, Medu, Fedu]
sample = pd.DataFrame([[4, 0, 2, 3, 3]], 
                       columns=["studytime", "failures", "absences", "Medu", "Fedu"])

# Predict
predicted_grade = model.predict(sample)[0]

print("=== Student Grade Prediction ===")
print(f"Study time   : 4 hrs/week")
print(f"Failures     : 0")
print(f"Absences     : 2 days")
print(f"Mother edu   : 3 (secondary)")
print(f"Father edu   : 3 (secondary)")
print(f"\nPredicted Final Grade: {predicted_grade:.1f} / 20")

if predicted_grade >= 10:
    print("Result: PASS")
else:
    print("Result: FAIL")