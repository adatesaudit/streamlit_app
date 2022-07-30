import streamlit as st
from time import sleep


st.title("My calculator")

first_number = st.text_input("Enter first number", "0")
second_number = st.text_input("Enter second number", "0")

operation = st.selectbox("Select operation:" , ["Addition", "Subtraction"])

if st.button("Perform operation"):
    with st.spinner("Computing reults..."):
        sleep(2)
        if operation == 'Addition':
            result = int(first_number) + int(second_number)
            st.success(f"Your result is: {result}")
        elif operation == "Subtraction":
            result = int(first_number) - int(second_number)
            st.success(f"Your result is: {result}")

