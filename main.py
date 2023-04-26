import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast App')
city = st.text_input('City:')
days = st.select_slider('Forecast Days', options=[1, 2, 3, 4, 5], help='Select the number of days you want forecasted')
option = st.selectbox('What do you want to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {city}')
if city:


    main_data = get_data(city, days, option)
    if option == 'Temperature':

        figure = px.line(main_data, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    elif option == 'Sky':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        image_paths = [images[condition] for condition in main_data]
        st.image(image_paths, width=115)
