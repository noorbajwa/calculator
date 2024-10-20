import streamlit as st

# Define the operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Streamlit App Interface
st.title("Simple Calculator")

# Input Fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Select an Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.success(f"The result is: {result}")
