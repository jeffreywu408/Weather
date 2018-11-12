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
        print("Unable to read key")
    return apiKey

def forecast(cityName):
    apiKey = getKey()
    if (apiKey == ""):
        return
    
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    
    completeURL = baseURL + "appid=" + apiKey + "&q=" + cityName + "&units=imperial"
    
    response = requests.get(completeURL) 
    weather = response.json()
    print(weather)
    
    if weather["cod"] == 200: 
        y = weather["main"]  
        temperature = y["temp"]
        humidiy = y["humidity"] 
        z = weather["weather"] 
        weather_description = z[0]["description"] 
    
        print("Temperature (in Farenheit) = " +
                        str(temperature) +
              "\n Humidity (in percentage) = " +
                        str(humidiy) +
              "\n Description = " +
                        str(weather_description))
    
    else:
        print(weather["message"])


def main():
    cityName = input("Enter city name: ")
    forecast(cityName)

if __name__ == '__main__':
    main()