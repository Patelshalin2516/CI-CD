import streamlit as st
from datetime import datetime

# Function to get greeting based on time
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "🌅 Good Morning"
    elif hour < 18:
        return "🌞 Good Afternoon"
    else:
        return "🌙 Good Evening"

# Function to return emoji based on age
def get_avatar(age):
    if age < 13:
        return "🧒"
    elif age < 20:
        return "🧑‍🎓"
    elif age < 40:
        return "🧑‍💻"
    elif age < 60:
        return "🧑‍🏫"
    else:
        return "🧓"

# Title and description
st.title("👋 Welcome to My Streamlit App")
st.write("This is a fun and interactive Streamlit app that greets you personally!")

# Input section
with st.form("user_form"):
    name = st.text_input("What's your name?", value="")
    age = st.slider("How old are you?", 0, 100, 25)
    submitted = st.form_submit_button("✨ Greet Me")

if submitted:
    greeting = get_greeting()
    avatar = get_avatar(age)
    st.success(f"{greeting}, {name or 'stranger'}! {avatar} You are {age} years young! 🎉")

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit")
