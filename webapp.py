import streamlit as st
import pickle
import pandas as pd
import os

# Title
st.title('🏏 IPL Win Predictor')

# Load Model Safely
MODEL_PATH = "mdl.pkl"
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        pipe = pickle.load(f)
else:
    st.error("Model file 'mdl.pkl' not found. Please upload it to the same directory.")
    st.stop()

# Teams & Cities
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# Input Section
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_city = st.selectbox('Select Host City', sorted(cities))
target = st.number_input('Target Score', min_value=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0)
with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets_fallen = st.number_input('Wickets Fallen', min_value=0, max_value=10)

# Predict Button
if st.button('Predict Probability'):
    # Calculations
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_remaining = 10 - wickets_fallen
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # Validation
    if balls_left <= 0 or wickets_remaining <= 0:
        st.warning("Invalid inputs: No balls or wickets remaining.")
    else:
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_remaining],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Prediction
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display
        st.subheader("📊 Win Probabilities:")
        st.success(f"✅ {batting_team}: {round(win * 100)}%")
        st.error(f"❌ {bowling_team}: {round(loss * 100)}%")
