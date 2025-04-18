import streamlit as st

# Title and description
st.title("👋 Welcome to My Streamlit App")
st.write("This is a simple interactive Streamlit example.")

# Input field
name = st.text_input("What's your name?", value="")

# Slider
age = st.slider("How old are you?", 0, 100, 25)

# Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("✨ Greet Me"):
        st.success(f"Hello, **{name or 'stranger'}**! You are {age} years young! 🎉")

with col2:
    if st.button("🔄 Reset"):
        st.experimental_rerun()

# Footer
st.markdown("---")
st.caption("🚀 Built with Streamlit")
