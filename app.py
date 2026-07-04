import streamlit as st
import joblib

# Load Trained Model
model = joblib.load("model.pkl")

# Title
st.title("💼 Employee Salary Prediction App")

st.write("Enter Employee Details")

# Inputs
age = st.number_input("Age", min_value=18, max_value=60, value=25)

experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=2)

education = st.selectbox(
    "Education Level",
    ["12th Pass", "Graduate", "Post Graduate"]
)

# Convert Education to Numeric
if education == "12th Pass":
    education_value = 12
elif education == "Graduate":
    education_value = 16
else:
    education_value = 18

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict([[age, experience, education_value]])

    st.success(f"Predicted Salary: ₹ {prediction[0]:,.2f}")