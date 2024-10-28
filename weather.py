import tkinter as tk
import requests
import _json

root = tk.Tk()
root.title("Weather")

page_label = tk.Label(root, text="Your Local Weather Forecast")
page_label.pack()

def getWeatherData(location):
    api_key = ""
    url = "url of the API>"
    response = requests.get(url, params={"api_key": api_key})
    data = response.json()
    temperature = data["temperature"]
    humidity = data["humidity"]
    weather_forecast = data["weather_forecast"]

root.mainloop()