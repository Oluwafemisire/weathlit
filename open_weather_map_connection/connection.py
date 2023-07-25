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
            url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric'
            response = self.http.request('GET', url)
            weather_data = json.loads(response.data.decode('utf-8'))
            data_list = weather_data['list']
            length = len(data_list)
            data = { 
                'temp': [],
                'pressure': [],
                'humidity': [],
            }
            for i in range(0, length, +7):
                data['temp'].append(data_list[i]['main']['temp'])
                data['pressure'].append(data_list[i]['main']['pressure'])
                data['humidity'].append(data_list[i]['main']['humidity'])
            return data
            
        return _get(city)
    
