
# Simple Calculator App

## Objective
The objective is to create a simple calculator application in Python that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. 

## Deploying the Calculator App with Streamlit
Follow these steps to deploy the calculator app using [Streamlit](https://streamlit.io/):

### 1. Install Dependencies
Ensure you have Python installed. Then, install Streamlit by running:
```bash
pip install streamlit
```

### 2. Create a Python File
Create a file named `app.py` and add the following code:
```python
import streamlit as st

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

st.title("Simple Calculator")
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)
operator = st.selectbox("Choose an operator", ['+', '-', '*', '/'])

if st.button("Calculate"):
    result = calculator(num1, num2, operator)
    st.write(f"### Result: {result}")
```

### 3. Run the Application Locally
Start the Streamlit app by running:
```bash
streamlit run app.py
```
This will open the app in your browser.

### 4. Deploy on Streamlit Cloud
1. Push your `app.py` to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Sign in and create a new app.
4. Select your repository and deploy it.

Now your calculator app is live and accessible online!

## Notes
- Ensure that the app is user-friendly by handling invalid inputs.
- Consider enhancing the UI with additional styling using Streamlit components.
- This app can be further extended to include more mathematical functions.


