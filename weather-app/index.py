import requests
from tkinter import *
from tkinter import messagebox

API_KEY = "ae2a0b0783c26f2da1386f42ae36fb88"

def get_current_weather_data(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "City field cannot be empty!")
        return

    try:
        data = get_current_weather_data(city)
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_label.config(text=f"Weather: {weather}")
        temp_label.config(text=f"Temperature: {temp}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
    except KeyError:
        messagebox.showerror("Error", "City not found")

root = Tk()
root.title("Weather App")

city_label = Label(root, text="Enter city:")
city_label.pack(pady=5)

city_entry = Entry(root, width=30)
city_entry.pack(pady=5)

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=5)

weather_label = Label(root, text="")
weather_label.pack(pady=5)

temp_label = Label(root, text="")
temp_label.pack(pady=5)

humidity_label = Label(root, text="")
humidity_label.pack(pady=5)

wind_label = Label(root, text="")
wind_label.pack(pady=5)

root.mainloop()
