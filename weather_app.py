import requests
import tkinter as tk
from tkinter import messagebox

# API Key for openweathermap
API_KEY = "YOUR_API_KEY"

# Base URL for API request
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# This function sends a request to the API and shows the weather result
def get_weather():
    city = city_entry.get()

    # Check if user entered a city name
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    # Data that will be sent to the API
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # use Celsius
        'lang': 'en'        # language for description
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # If API result found successfully
        if data.get('cod') == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            result_label.config(text=f"Temperature: {temp}°C\nWeather: {desc}")
        else:
            messagebox.showerror("Error", "City not found!")

    except Exception:
        messagebox.showerror("Error", "Check your internet connection!")


# Creating main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.resizable(False, False)

# Set application icon
try:
    icon = tk.PhotoImage(file="logo.png")
    root.iconphoto(False, icon)
except:
    pass  # If icon not found, skip without error

# Input box for city name
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)

# Button to send request
search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=5)

# Label to show temperature and weather status
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
