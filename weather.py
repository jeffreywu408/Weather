#!/usr/local/bin/python3
import requests

def getKey():
    apiKey = ""
    try:
        f=open("key", "r")
        if f.mode == 'r':
            apiKey = f.read()
        f.close()
    except:
        print("Invalid API key")
    return apiKey

def main():
    apiKey = getKey()
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
     
    cityName = input("Enter city name : ") 
    
    completeURL = baseURL + "appid=" + apiKey + "&q=" + cityName + "&units=imperial"
    
    response = requests.get(completeURL) 
    weather = response.json()
    print(weather)
    
    
    if weather["cod"] != "404": 
        y = weather["main"]  
        temperature = y["temp"] 
        pressure = y["pressure"] 
        humidiy = y["humidity"] 
        z = weather["weather"] 
        weather_description = z[0]["description"] 
    
        print(" Temperature (in Farenheit) = " +
                        str(temperature) + 
              "\n Atmospheric Pressure (in millibars) = " +
                        str(pressure) +
              "\n Humidity (in percentage) = " +
                        str(humidiy) +
              "\n Description = " +
                        str(weather_description))
    else:
        print(" City Not Found ")


if __name__ == '__main__':
    main()