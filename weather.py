# I start with importing Tkinter for our Python window
import tkinter as tk
#I import requests to get API Keys for our Weather App
import requests
#I import Java Script for our weather app
import _json

#First I add root window as Tk
root = tk.Tk()
#I add a title for our window
root.title("Weather")
#I create a label for the page we created named Local Weather
page_label = tk.Label(root, text="Your Local Weather Forecast")
page_label.pack()
#Here is the fuction I created to get the weather api key from the users local area
def getWeatherData(location):
    api_key = ""
    url = "url of the API>"
    response = requests.get(url, params={"api_key": api_key})
    data = response.json()
    temperature = data["temperature"]
    humidity = data["humidity"]
    weather_forecast = data["weather_forecast"]
#I make sure to close out our window with root.mainloop()
root.mainloop()