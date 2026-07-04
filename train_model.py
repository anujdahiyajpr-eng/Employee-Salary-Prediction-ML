import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load Dataset
data = pd.read_csv("data/salary_data.csv")

# Input Features
X = data[['Age', 'Experience', 'Education']]

# Target
y = data['Salary']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model Trained Successfully!")
print("model.pkl file created.")