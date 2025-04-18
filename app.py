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
        return "🧑‍🎓done"
    elif age < 40:
        return "🧑‍💻"
    elif age < 60:
        return "🧑‍🏫"
    else:
        return "🧓"

# Function to change background color based on age
def get_background_color(age):
    if age < 13:
        return "#FFE0B2"  # Light Yellow for kids
    elif age < 20:
        return "#C8E6C9"  # Light Green for teens
    elif age < 40:
        return "#BBDEFB"  # Light Blue for young adults
    elif age < 60:
        return "#FFF59D"  # Light Yellow for adults
    else:
        return "#D1C4E9"  # Light Purple for seniors

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
    bg_color = get_background_color(age)

    # Change background color dynamically
    st.markdown(f"<style>body{{background-color: {bg_color};}}</style>", unsafe_allow_html=True)

    # Display greeting
    st.success(f"{greeting}, {name or 'stranger'}! {avatar} You are {age} years young! 🎉")

    # Age-based recommendation
    if age < 18:
        st.write("👨‍🎓 Keep up the studies! 📚")
    elif age < 40:
        st.write("💼 Focus on building your career and skills!")
    elif age < 60:
        st.write("🌱 Enjoy the journey and growth!")
    else:
        st.write("🌟 Enjoy the golden years with peace and joy!")

# Reset button to clear input
if st.button("🔄 Reset"):
    st.experimental_rerun()

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit")
