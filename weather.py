import tkinter as tk
import requests


def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")
    else:
        weather_label.config(text="Error fetching weather data.")


# Create the main window
window = tk.Tk()
window.title("Weather App")

# City entry
city_label = tk.Label(window, text="Enter city:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

# Get weather button
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Weather label
weather_label = tk.Label(window, text="")
weather_label.pack()

window.mainloop()