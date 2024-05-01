import streamlit as st


st.title("Five Day Weather Forecast")
place = st.text_input("City: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                                help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
