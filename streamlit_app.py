import streamlit as st
import pandas as pd
import requests

st.title("Airbnb Price Prediction")

# Example fields (simplify as needed)
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
neighbourhood = st.text_input("Neighbourhood", "THIRD WARD")
minimum_nights = st.number_input("Minimum Nights", min_value=1, value=2)
availability_365 = st.number_input("Availability (days per year)", min_value=0, max_value=365, value=180)
reviews_density = st.number_input("Reviews Density", min_value=0.0, value=1.0)
price_per_min_night = st.number_input("Price per Minimum Night", min_value=0.0, value=100.0)
is_professional_host = st.selectbox("Is Professional Host?", [0, 1])
days_since_last_review = st.number_input("Days Since Last Review", min_value=0.0, value=50.0)
popularity_score = st.number_input("Popularity Score", min_value=0.0, value=1.0)
latitude = st.number_input("Latitude", value=42.65)
longitude = st.number_input("Longitude", value=-73.75)

if st.button("Predict"):
    data = {
        "room_type": room_type,
        "neighbourhood": neighbourhood,
        "minimum_nights": minimum_nights,
        "availability_365": availability_365,
        "reviews_density": reviews_density,
        "price_per_min_night": price_per_min_night,
        "is_professional_host": is_professional_host,
        "days_since_last_review": days_since_last_review,
        "popularity_score": popularity_score,
        "latitude": latitude,
        "longitude": longitude
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Log Price: {result['predicted_log_price']:.2f}$")
    else:
        st.error("Error in prediction request.")
