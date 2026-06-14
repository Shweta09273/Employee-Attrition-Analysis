import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("data/emp_attrition.csv")

print("Dataset Shape:", df.shape)

# Encode categorical columns
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and Target
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nTop 10 Important Features:")
print(importance.sort_values("Importance", ascending=False).head(10))
top_features = importance.sort_values(
    by="Importance",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.barh(top_features["Feature"],
         top_features["Importance"])
plt.title("Top 10 Important Features")
plt.tight_layout()
plt.show()