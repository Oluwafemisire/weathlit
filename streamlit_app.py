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
def get_weather_data(city):
    data = accessor.get(city)
    return data

city = st.text_input('City')


with st.spinner('Getting weather results...'):
    if city:
        try:
            data = get_weather_data(city)
            temp = data['temp']
            pressure = data['pressure']
            humidity = data['humidity']
            wind_speed = data['wind_speed']

            st.metric('Temperature', f'{temp} °C')
            st.metric('Pressure', f'{pressure} hPa')
            st.metric('Humidity', f'{humidity} %')
            st.metric('Wind Speed', f'{wind_speed} m/s')
        except:
            st.error('City not found')

