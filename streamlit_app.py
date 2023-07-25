import streamlit as st
from open_weather_map_connection.connection import WeatherMapConnection

st.set_page_config(
    page_title = 'Open Weather Map Data',
    page_icon = '🌤️',
)

st.title('Open Weather Map Data')

"""
This MVP demo uses the [Open Weather Map API](https://openweathermap.org/api) to get weather data for a given city.

You can find link to the repo [here](https://github.com/Oluwafemisire/weathlit).

But for now where would you like to get weather data for?
"""
conn = st.experimental_connection('weathermap', type=WeatherMapConnection)
accessor = conn.accessor()

city = st.text_input('City')


with st.spinner('Getting weather results...'):
    if city:
        try:
            """
            The weather forecast for the next 5 days is shown below."""
            data = accessor.get(city)
            temp = data['temp']
            pressure = data['pressure']
            humidity = data['humidity']
            
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric('Temperature', f'{temp[0]} °C')
            with col2:
                st.metric('Temperature', f'{temp[1]} °C')
            with col3:
                st.metric('Temperature', f'{temp[2]} °C')
            with col4:
                st.metric('Temperature', f'{temp[3]} °C')
            with col5:
                st.metric('Temperature', f'{temp[4]} °C')

            st.line_chart(temp)
            
            col6, col7, col8, col9, col10 = st.columns(5)
            with col6:
                st.metric('Pressure', f'{pressure[0]} Pa')
            with col7:
                st.metric('Pressure', f'{pressure[1]} Pa')
            with col8:
                st.metric('Pressure', f'{pressure[2]} Pa')
            with col9:
                st.metric('Pressure', f'{pressure[3]} Pa')
            with col10:
                st.metric('Pressure', f'{pressure[4]} Pa')

            st.line_chart(pressure)
            
            col11, col12, col13, col14, col15 = st.columns(5)
            with col11:
                st.metric('Humidity', f'{humidity[0]} %')
            with col12:
                st.metric('Humidity', f'{humidity[1]} %')
            with col13:
                st.metric('Humidity', f'{humidity[2]} %')
            with col14:
                st.metric('Humidity', f'{humidity[3]} %')
            with col15:
                st.metric('Humidity', f'{humidity[4]} %')

            st.line_chart(humidity)

        except:
            st.error('Error')
            
        
