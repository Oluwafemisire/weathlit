
# Open Weather Map Data Streamlit Application

This Streamlit application provides a user-friendly interface to access weather data for a given city using the Open Weather Map API.

You can check out the deployed app here: [Weathlit](https://weathlit.streamlit.app/).
![image](https://github.com/Oluwafemisire/weathlit/assets/66549203/fbdd3bb3-e0bc-4071-b70f-d852d9b8a6e4)

## About Project

This project demonstrates a minimum viable product (MVP) using Streamlit, a Python library for creating web applications for data science and machine learning projects. The application connects to the Open Weather Map API to fetch real-time weather data for a given city and presents it in a user-friendly manner.

## Navigating the app

Upon launching the application, you will see a text input field where you can enter the name of the city for which you want to fetch weather data.

Type the name of the desired city in the text input and press "Enter" or click outside the input to trigger the data retrieval process.

The application will fetch weather data for the specified city using the Open Weather Map API and display the weather forecast for 5  days.

You can view the temperature, pressure, and humidity metrics in both numerical and chart format.

## Getting Started Locally

Follow the instructions below to run the Streamlit application on your local machine:

1. Clone the GitHub repository: [Open Weather Map Streamlit](https://github.com/Oluwafemisire/weathlit).

2. Ensure that you have streamlit installed on your local machine. Find out how to install streamlit [here](https://docs.streamlit.io/library/get-started/installation)
3. Create a .streamlit folder in your root directory
4. Navigate to your .streamlit directory
```bash
cd .streamlit
```
5. Create a secrets.toml file and place your open weather api key. Find out more here [Open weather Map API](https://openweathermap.org/)
```bash
apikey = 'YOUR API KEY'
```
6. Run the following command in your terminal from your root terminal using windows.
```bash
streamlit run streamlit_app.py
```

## Acknowledgements
The weather data is provided by [Open Weather Map](https://openweathermap.org/), which offers a powerful and reliable weather API for developers.


Special thanks to the Streamlit team for providing an excellent framework for building interactive and intuitive web applications in Python.


Enjoy exploring the weather data and have a great day! 🌞🌤️🌦️
