import streamlit as st
import requests
from datetime import datetime, time
import json

# Configure the app
st.set_page_config(
    page_title="Daily Tracker",
    page_icon="📊",
    layout="wide"
)

# API endpoint
API_URL = "http://localhost:8000/api"

def main():
    st.title("Daily Tracker 📊")
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Daily Entry", "Meals", "Review"])

    with tab1:
        st.header("Today's Entry")
        
        # Create two columns for mood and energy
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Mood")
            mood_score = st.slider("How's your mood?", 1, 10, 5)
            mood_notes = st.text_area("Any notes about your mood?")

        with col2:
            st.subheader("Energy")
            energy_score = st.slider("Energy level", 1, 10, 5)
            energy_notes = st.text_area("Any notes about your energy?")

        # Sleep tracking
        st.subheader("Sleep")
        col3, col4 = st.columns(2)
        
        with col3:
            sleep_time = st.time_input("What time did you go to bed?", time(22, 0))
            sleep_quality = st.slider("Sleep quality", 1, 10, 5)

        with col4:
            wake_time = st.time_input("What time did you wake up?", time(7, 0))
            sleep_notes = st.text_area("Any notes about your sleep?")

        # Productivity
        st.subheader("Productivity")
        productivity_score = st.slider("How productive were you today?", 1, 10, 5)
        productivity_notes = st.text_area("Notes about your productivity")

        # General notes
        st.subheader("General Notes")
        general_notes = st.text_area("Anything else you want to note about today?")

        if st.button("Save Daily Entry"):
            # Combine date and time for sleep_time and wake_time
            today = datetime.now().date()
            sleep_datetime = datetime.combine(today, sleep_time)
            wake_datetime = datetime.combine(today, wake_time)
            
            # Create entry data
            entry_data = {
                "mood_score": mood_score,
                "energy_score": energy_score,
                "productivity_score": productivity_score,
                "mood_elaboration": mood_notes,
                "energy_elaboration": energy_notes,
                "productivity_elaboration": productivity_notes,
                "general_notes": general_notes,
                "sleep_time": sleep_datetime.isoformat(),
                "wake_time": wake_datetime.isoformat(),
                "sleep_quality": sleep_quality,
                "sleep_notes": sleep_notes
            }

            try:
                response = requests.post(f"{API_URL}/daily-entries/", json=entry_data)
                if response.status_code == 200:
                    st.success("Entry saved successfully!")
                else:
                    st.error(f"Error saving entry: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to API: {str(e)}")

    with tab2:
        st.header("Meal Tracking")
        
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"])
        meal_time = st.time_input("Meal Time")
        meal_description = st.text_area("What did you eat?")
        satisfaction_score = st.slider("How satisfied were you with this meal?", 1, 10, 5)

        if st.button("Add Meal"):
            # TODO: Implement meal addition logic
            st.info("Meal tracking will be implemented in the next update!")

    with tab3:
        st.header("Daily Review")
        # TODO: Add visualization of recent entries
        st.info("Daily review features coming soon!")

if __name__ == "__main__":
    main()