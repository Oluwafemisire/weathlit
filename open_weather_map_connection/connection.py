from streamlit.connections import ExperimentalBaseConnection
import urllib3
import json
import streamlit as st

class WeatherMapConnection(ExperimentalBaseConnection):
    def _connect(self, **kwargs):
        self.http = urllib3.PoolManager()
        self.api_key = st.secrets['apikey']

    def accessor(self):
        return self
        
    def get(self, city):
        @st.cache_data    
        def _get(city):
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric'
            response = self.http.request('GET', url)
            weather_data = json.loads(response.data.decode('utf-8'))
            lon = weather_data['coord']['lon']
            lat = weather_data['coord']['lat']
            temp = weather_data['main']['temp']
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            return {
                'lon': lon,
                'lat': lat,
                'temp': temp,
                'pressure': pressure,
                'humidity': humidity,
                'wind_speed': wind_speed            
                }
        return _get(city)
    
