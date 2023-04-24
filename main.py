import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast App')
city = st.text_input('City:')
days = st.select_slider('Forecast Days', options=[1, 2, 3, 4, 5], help='Select the number of days you want forecasted')
option = st.selectbox('What do you want to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {city}')

main_data = get_data(place, days, type_)
figure = px.line(x=dates, y=temperatures, labels={'x':'Date', 'y': 'Temperature (C)' })
st.plotly_chart(figure)
