#!/usr/local/bin/python3
import requests
import re


def getKey():
    apiKey = ""
    try:
        f = open("key", "r")
        if f.mode == 'r':
            apiKey = f.read().replace('\n', '')
        f.close()
    except:
        print("Unable to read key")
    return apiKey


def forecast(cityName):
    apiKey = getKey()
    if (apiKey == ""):
        return

    # regex for ZIP Code
    pattern = "^\d{5}(?:[-\s]\d{4})?$"
    zip = re.match(pattern, cityName)

    if zip is None:
        currentURL = "https://api.openweathermap.org/data/2.5/weather?APPID=" + apiKey + "&units=imperial" + "&q=" + cityName
        w = requests.get(currentURL).json()

        forecastURL = "https://api.openweathermap.org/data/2.5/forecast?appid=" + apiKey + "&units=imperial" + "&q=" + cityName
        f = requests.get(forecastURL).json()
    else:
        currentURL = "https://api.openweathermap.org/data/2.5/weather?APPID=" + apiKey + "&units=imperial" + "&zip=" + cityName
        w = requests.get(currentURL).json()

        forecastURL = "https://api.openweathermap.org/data/2.5/forecast?appid=" + apiKey + "&units=imperial" + "&zip=" + cityName
        f = requests.get(forecastURL).json()

    if w["cod"] >= 200 and w["cod"] < 300:
        city = str(w['name'])
        country = str(w['sys']['country'])
        temp = str(w["main"]["temp"])
        humidity = str(w["main"]["humidity"])
        description = str(w["weather"][0]["description"])

        print("Current Weather Conditions in " + city + ", " + country)
        print("Temperature = " + temp + "F" +
              "\nHumidity = " + humidity + "%" +
              "\nDescription = " + description + "\n")
    else:
        print(w["message"])
        return

    currentDate = ""
    for i in f["list"]:
        # dt_txt is in format [YYYY-MM-DD HH:MM:SS]
        time = i["dt_txt"]

        # nextDate = YYYY-MM-DD, hour = HH:MM:SS
        nextDate, hour = time.split(" ")

        # Only print each date once
        if currentDate != nextDate:
            currentDate = nextDate
            year, month, day = currentDate.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('{m}/{d}/{y}'.format(**date))

        # Convert hour from 24 hour clock to 12 hour clock
        hour = int(hour[:2])
        if hour < 12:
            if hour == 0:
                hour = 12
            print('%i:00 am' % hour)
        else:
            if hour > 12:
                hour -= 12
            print('%i:00 pm' % hour)

        temp = str(i['main']['temp'])
        humidity = str(i["main"]["humidity"])
        description = str(i['weather'][0]['description'])

        print("Temperature = " + temp + "F" +
              "\nHumidity = " + humidity + "%" +
              "\nDescription = " + description + "\n")


def main():
    cityName = input("Enter City Name or ZIP Code: ")
    forecast(cityName)


if __name__ == '__main__':
    main()
