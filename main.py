import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Five Day Weather Forecast")
place = st.text_input("City: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                                help="Select the number of days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
