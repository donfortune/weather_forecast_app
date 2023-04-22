import streamlit as st

st.title('Weather Forecast App')
city = st.text_input('City:')
days = st.select_slider('Forecast Days', options=[1, 2, 3, 4, 5], help='Select the number of days you want forecasted')
option = st.selectbox('What do you want to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {city}')

