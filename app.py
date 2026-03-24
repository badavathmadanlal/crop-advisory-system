import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import geocoder
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- THEME ----------------
theme = st.sidebar.selectbox("Theme", ["Dark", "Light"])

if theme == "Light":
    st.markdown("""
    <style>
    body {background-color: #ffffff; color: black;}
    </style>
    """, unsafe_allow_html=True)

# ---------------- LANGUAGE ----------------
lang = st.sidebar.radio("Language", ["English", "Telugu"])

TEXT = {
    "title": {"en": "🌱 Crop Advisory System", "te": "🌱 పంట సూచన వ్యవస్థ"},
    "prediction": {"en": "🌾 Prediction", "te": "🌾 అంచనా"},
    "dashboard": {"en": "📊 Dashboard", "te": "📊 డాష్‌బోర్డ్"},
    "contact": {"en": "📞 Contact Us", "te": "📞 సంప్రదించండి"},
    "location": {"en": "📍 Location", "te": "📍 స్థానం"},
    "season": {"en": "Select Season", "te": "సీజన్ ఎంచుకోండి"},
}

def t(key):
    return TEXT[key]["en"] if lang == "English" else TEXT[key]["te"]

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_crop_data.csv")

data = load_data()

# ---------------- LOCATION ----------------
def get_location():
    try:
        g = geocoder.ip('me')
        return g.city, g.latlng
    except:
        return "India", [22.5937, 78.9629]

# ---------------- WEATHER ----------------
def get_weather(city):
    api_key = "e5c6719be1fd15ba3eea045ebe0357b0"
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        res = requests.get(url).json()
        temp = res["main"]["temp"] - 273
        humidity = res["main"]["humidity"]
        return round(temp,2), humidity
    except:
        return None, None

# ---------------- SEASON DATA ----------------
def season_data(season):
    if season == "Kharif":
        return {"N": 80, "P": 40, "K": 40, "Temp": "25-35°C", "Rainfall": "200-300 mm"}
    elif season == "Rabi":
        return {"N": 60, "P": 30, "K": 30, "Temp": "10-25°C", "Rainfall": "50-100 mm"}
    else:
        return {"N": 50, "P": 25, "K": 25, "Temp": "20-30°C", "Rainfall": "100-200 mm"}

# ---------------- NAVIGATION ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "Dashboard", "Contact"])

# ---------------- HOME ----------------
if page == "Home":
    st.title(t("title"))

# ---------------- WELCOME SCROLL ----------------
    st.markdown("""
    <div style="
        background-color:#2c7a7b;
        padding:10px;
        border-radius:10px;
        color:white;
        font-size:20px;
        text-align:center;
        animation: scrollText 10s linear infinite;
    ">
        Welcome to Crop Advisory System | Helping Farmers with Smart Decisions 🌱
    </div>

    <style>
    @keyframes scrollText {
        0% {transform: translateX(100%);}
        100% {transform: translateX(-100%);}
    }
    </style>
    """, unsafe_allow_html=True)


    city, coords = get_location()
    temp, hum = get_weather(city)

    st.write(t("location"), city)

    if temp:
        st.write("🌡 Temp:", temp, "°C")
        st.write("💧 Humidity:", hum, "%")

    # INDIA MAP (FIXED)
    st.subheader("India Map")

    map_data = pd.DataFrame({
        "lat": [coords[0]],
        "lon": [coords[1]],
        "city": [city]
    })

    fig = px.scatter_mapbox(
        map_data,
        lat="lat",
        lon="lon",
        hover_name="city",
        zoom=4,
        height=700
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_center={"lat": 22.5937, "lon": 78.9629}
    )

    col1, col2, col3 = st.columns([0.5,4,0.5])

    with col2:
        st.plotly_chart(fig)
# ---------------- PREDICTION ----------------
elif page == "Prediction":
    st.title(t("prediction"))

    season = st.selectbox(t("season"), ["Kharif", "Rabi", "Summer"])
    values = season_data(season)

    st.subheader("Recommended Conditions")
    st.write("Nitrogen:", values["N"])
    st.write("Phosphorus:", values["P"])
    st.write("Potassium:", values["K"])
    st.write("Temperature:", values["Temp"])
    st.write("Rainfall:", values["Rainfall"])

# ---------------- DASHBOARD ----------------
elif page == "Dashboard":
    st.title(t("dashboard"))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Crop Distribution")
        fig, ax = plt.subplots()
        data["label"].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("Temperature vs Crop")
        fig, ax = plt.subplots()
        sns.boxplot(x="label", y="temperature", data=data)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Rainfall vs Crop")
        fig, ax = plt.subplots()
        sns.boxplot(x="label", y="rainfall", data=data)
        plt.xticks(rotation=90)
        st.pyplot(fig)

    with col4:
        st.subheader("NPK Distribution")
        fig, ax = plt.subplots()
        data[["n","p","k"]].plot(kind="box", ax=ax)
        st.pyplot(fig)

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Soil pH Distribution")
        fig, ax = plt.subplots()
        data["ph"].hist(ax=ax)
        st.pyplot(fig)

    with col6:
        st.subheader("Correlation Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(data.select_dtypes(include=['int64','float64']).corr(), annot=True, ax=ax)
        st.pyplot(fig)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.title(t("contact"))

    states = ["Andhra Pradesh", "Telangana", "Tamil Nadu", "Karnataka"]
    districts = ["Hyderabad", "Warangal", "Chennai", "Bangalore"]
    villages = ["Village A", "Village B", "Village C"]

    name = st.text_input("Person Name")
    phone = st.text_input("Phone Number")

    state_input = st.text_input("State")
    suggestions = [s for s in states if state_input.lower() in s.lower()]
    if suggestions:
        st.write("Suggestions:", suggestions)

    district = st.selectbox("District", districts)
    village = st.selectbox("Village", villages)

    if st.button("Submit"):
        st.success("Submitted successfully")


