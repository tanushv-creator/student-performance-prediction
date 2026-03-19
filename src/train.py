import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Load clean data
df = pd.read_csv("data/processed/student_clean.csv")

# Features and target
X = df[["studytime", "failures", "absences", "Medu", "Fedu"]]
y = df["G3"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

best_model = None
best_r2 = -999

print("=== Model Results ===\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds) ** 0.5
    r2 = r2_score(y_test, preds)
    print(f"{name}")
    print(f"  RMSE : {rmse:.2f}")
    print(f"  R2   : {r2:.2f}\n")
    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_name = name

# Save best model
os.makedirs("models", exist_ok=True)
joblib.dump(best_model, "models/best_model.pkl")
print(f"Best model: {best_name} (R2: {best_r2:.2f})")
print("Saved to models/best_model.pkl")