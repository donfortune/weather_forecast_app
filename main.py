import streamlit as st
import plotly.express as px

st.title('Weather Forecast App')
city = st.text_input('City:')
days = st.select_slider('Forecast Days', options=[1, 2, 3, 4, 5], help='Select the number of days you want forecasted')
option = st.selectbox('What do you want to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {city}')

dates = ['2023-25-10', '2023-26-10', '2023-27-10']
temperatures = [10, 11, 15]
temperatures = [days * i for i in temperatures]
figure = px.line(x=dates, y=temperatures, labels={'x':'Date', 'y': 'Temperature (C)' })
st.plotly_chart(figure)
