import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyD0tu_EpumJhb9Ep0lFVlbnMg33ucCjy8s")

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("🧮 AI Calculator")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
operation = st.selectbox("Select the operation:", ["Addition", "Subtraction", "Multiplication", "Division"])
if st.button("Calculate"):
    if operation == "Addition":
        prompt = f"What is {num1} + {num2}?"
    elif operation == "Subtraction":
        prompt = f"What is {num1} - {num2}?"
    elif operation == "Multiplication":
        prompt = f"What is {num1} * {num2}?"
    else:
        prompt = f"What is {num1} / {num2}?"
    
    response = model.generate_content(prompt)
    st.write(f"The result of {operation.lower()} is: {response.text.strip()}")
    