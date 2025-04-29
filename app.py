import streamlit as st

# Setting the title
st.title("What time should I leave?")

# Description
st.write("Find the best time to leave ~")

# Create a text input box for the starting location
start_location = st.text_input("Enter the starting location:")

# Create a text input box for the ending location
end_location = st.text_input("Enter the destination:")

# Mode of transport:
transport_mode = st.selectbox(
    "select your mode of transport:",
    ("Driving", "Public Transport", "Walking", "Biking")
)

# Add a button to submit:
if st.button("What Time Should I Leave?"):
    st.write("Fetching best time to leave... (placeholder)")