import streamlit as st
from datetime import datetime
from geoip2.database import Reader
import streamlit.web.server.websocket_headers as wh

# --- Config ---
BLOCKED_COUNTRIES = {'CA', 'JP'}  # Canada, Japan

# --- Load GeoIP Reader only once ---
@st.cache_resource
def load_geoip_reader():
    return Reader("GeoLite2-Country.mmdb")

geoip_reader = load_geoip_reader()

# --- IP Utilities ---
def get_real_ip():
    headers = wh._get_websocket_headers()
    ip = headers.get("X-Forwarded-For", "")
    return ip.split(",")[0].strip() if ip else None

def is_blocked_country(ip):
    try:
        response = geoip_reader.country(ip)
        return response.country.iso_code in BLOCKED_COUNTRIES
    except Exception:
        return False

# --- GeoIP Block ---
user_ip = get_real_ip()
if user_ip and is_blocked_country(user_ip):
    st.error("🚫 Access from your country is not allowed.")
    st.stop()

# --- Greeting Functions ---
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "🌅 Good Morning"
    elif hour < 18:
        return "🌞 Good Afternoon"
    else:
        return "🌙 Good Evening"

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

def get_background_color(age):
    if age < 13:
        return "#FFE0B2"
    elif age < 20:
        return "#C8E6C9"
    elif age < 40:
        return "#BBDEFB"
    elif age < 60:
        return "#FFF59D"
    else:
        return "#D1C4E9"

# --- App UI ---
st.title("👋 Welcome to My Streamlit App")
st.write("This is a fun and interactive Streamlit app that greets you personally!")

with st.form("user_form"):
    name = st.text_input("What's your name?", value="")
    age = st.slider("How old are you?", 0, 100, 25)
    submitted = st.form_submit_button("✨ Greet Me")

if submitted:
    greeting = get_greeting()
    avatar = get_avatar(age)
    bg_color = get_background_color(age)

    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

    st.success(f"{greeting}, {name or 'stranger'}! {avatar} You are {age} years young! 🎉")

    if age < 18:
        st.write("👨‍🎓 Keep up the studies! 📚")
    elif age < 40:
        st.write("💼 Focus on building your career and skills!")
    elif age < 60:
        st.write("🌱 Enjoy the journey and growth!")
    else:
        st.write("🌟 Enjoy the golden years with peace and joy!")

if st.button("🔄 Reset"):
    st.experimental_rerun()

st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit")
