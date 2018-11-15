#!/usr/local/bin/python3
import requests

def getKey():
    apiKey = ""
    try:
        f=open("key", "r")
        if f.mode == 'r':
            apiKey = f.read().replace('\n','')
        f.close()
    except:
        print("Unable to read key")
    return apiKey

def forecast(cityName):
    apiKey = getKey()
    if (apiKey == ""):
        return
    
    baseURL = "https://api.openweathermap.org/data/2.5/weather?"
    
    completeURL = baseURL + "APPID=" + apiKey + "&units=imperial" + "&q=" + cityName
    
    response = requests.get(completeURL)
    w = response.json()
    
    if w["cod"] >= 200 and w["cod"] < 300: 
        print("Current Weather Conditions")
        print("Temperature = " + str(w["main"]["temp"]) + "F" +
              "\nHumidity = " + str(w["main"]["humidity"]) + "%" +
              "\nDescription = " + str(w["weather"][0]["description"]))
    else:
        print(w["message"])


def main():
    cityName = input("Enter city name: ")
    forecast(cityName)

if __name__ == '__main__':
    main()