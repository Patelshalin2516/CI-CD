import streamlit as st

# Title and description
st.title("Welcome to My Streamlit App")
st.write("This is a basic Streamlit page example.")

# Input field
name = st.text_input("Enter your name:")

# Slider
age = st.slider("Select your age:", 0, 100, 25)

# Button
if st.button("Greet Me"):
    st.success(f"Hello {name}, you are {age} years old!")

# Footer
st.markdown("---")
st.caption("Built with using Streamlit")
