from tkinter import *
import requests
import json
#function to convert kelvin to celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Creating the object for the tkinter module
root = Tk()
# setting the title for appl;ication
root.title("Weather App")
# setting window size
root.geometry("500x500")
#setting window color
root['background'] = "white"



# City Search
city_var = StringVar()
city_entry = Entry(root, textvariable=city_var, width=45)

city_entry.grid(row=1, column=0)

def fetch_weather():
    # Retrieve API Key from environment variable
    api_key = '30d4741c779ba94c470ca1f63045390a'  # Set your API key in the system environment
    city = city_var.get()
    
    # API Call
    try:
        api_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        api = json.loads(api_request.content)

        if api['cod'] != 200:  # Check if the response is successful
            raise ValueError(api.get('message', 'Error retrieving data'))

        # Temperatures
        main_data = api['main']
        current_temperature = kelvin_to_celsius(main_data['temp'])
        humidity = main_data['humidity']
        temp_min = kelvin_to_celsius(main_data['temp_min'])
        temp_max = kelvin_to_celsius(main_data['temp_max'])

        # Coordinates
        coords = api['coord']
        longitude = coords['lon']
        latitude = coords['lat']

        # Country and City
        country = api['sys']['country']
        city_name = api['name']

        # Updating the labels with the retrieved info
        label_temp['text'] = f"{current_temperature:.2f} °C"
        label_humidity['text'] = f"{humidity}%"
        max_temp['text'] = f"{temp_max:.2f} °C"
        min_temp['text'] = f"{temp_min:.2f} °C"
        label_lon['text'] = longitude
        label_lat['text'] = latitude
        label_country['text'] = country
        label_city['text'] = city_name
    except Exception as e:
        label_temp['text'] = "Error"
        label_humidity['text'] = ""
        max_temp['text'] = ""
        min_temp['text'] = ""
        label_lon['text'] = ""
        label_lat['text'] = ""
        label_country['text'] = ""
        label_city['text'] = str(e)

# Search Bar and Button
city_button = Button(root, text="Search", command=fetch_weather)
city_button.grid(row=1, column=1)

# Country Names and Coordinates
label_city = Label(root, text="...", width=0, bg='white', font=("bold", 15))
label_city.place(x=15, y=63)

label_country = Label(root, text="...", width=0, bg='white', font=("bold", 15))
label_country.place(x=180, y=63)

label_lon = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
label_lon.place(x=15, y=95)

label_lat = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
label_lat.place(x=180, y=95)

# Current Temperature
label_temp = Label(root, text="...", width=0, bg="White", font=("Hahmlet", 55), fg='black')
label_temp.place(x=18, y=250)

# Other temperature details
label_humidity = Label(root, text="Humidity : ", bg='white', font=("bold", 15))
label_humidity.place(x=15, y=400)

humidity_value = Label(root, text="...", width=0, bg='white', font=("bold", 15))
humidity_value.place(x=130, y=400)

# Maximum Temperature
max_label = Label(root, text="Max.Temp.: ", bg='white', font=("bold", 15))
max_label.place(x=15, y=430)

max_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

# Minimum Temperature
min_label = Label(root, text="Min.Temp.: ", bg='white', font=("bold", 15))
min_label.place(x=15, y=460)

min_temp = Label(root, text="...", width=0, bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

root.mainloop()
