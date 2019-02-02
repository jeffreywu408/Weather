#!/usr/local/bin/python3
import requests
import re


def get_key():
    api_key = ""
    try:
        f = open("key", "r")
        if f.mode == 'r':
            api_key = f.read().replace('\n', '')
        f.close()
    except IOError:
        print("Unable to read key")
    return api_key


def forecast(city_name):
    api_key = get_key()
    if api_key == "":
        return

    # regex for ZIP Code
    pattern = "^\d{5}(?:[-\s]\d{4})?$"
    zip_code = re.match(pattern, city_name)

    if zip_code is None:
        current_url = \
            "https://api.openweathermap.org/data/2.5/weather?APPID=" \
            + api_key + "&units=imperial" + "&q=" + city_name
        w = requests.get(current_url).json()

        forecast_url = \
            "https://api.openweathermap.org/data/2.5/forecast?appid=" \
            + api_key + "&units=imperial" + "&q=" + city_name
        f = requests.get(forecast_url).json()

    else:
        current_url = \
            "https://api.openweathermap.org/data/2.5/weather?APPID=" \
            + api_key + "&units=imperial" + "&zip=" + city_name
        w = requests.get(current_url).json()

        forecast_url = \
            "https://api.openweathermap.org/data/2.5/forecast?appid=" \
            + api_key + "&units=imperial" + "&zip=" + city_name
        f = requests.get(forecast_url).json()

    if 200 <= w["cod"] < 300:
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

    current_date = ""
    for i in f["list"]:
        # dt_txt is in format [YYYY-MM-DD HH:MM:SS]
        time = i["dt_txt"]

        # nextDate = YYYY-MM-DD, hour = HH:MM:SS
        next_date, hour = time.split(" ")

        # Only print each date once
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
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
    city_name = input("Enter City Name or ZIP Code: ")
    forecast(city_name)


if __name__ == '__main__':
    main()
