import json
import requests

def direction(int):
    if int > 315 or int < 45 :
        return "N"
    elif 45 < int and int < 135 :
        return "E"
    elif 135 < int and int < 225 :
        return "S"
    elif 225 < int and int < 315 :
        return "W"
    return;

print("How would you want to find the location:")
print("1. City name\n2. Code\n3. ZIP code")
x = int(input())
a = ""

while x > 3 or x <1 :
    print("\nWrong entry; try again: ")
    input(x)

if x == 1: 
    print("\nEnter the city name: ")
    a = input()
    query = {'q': a, 'limit' : 1, 'appid' : '1156d71518eb434f16df8c9eed318677'}
    respond = requests.get("http://api.openweathermap.org/geo/1.0/direct?", params = query)
    tempdict = respond.json()
    latcoord = tempdict[0]["lat"]
    loncoord = tempdict[0]["lon"]
    finalquery = {'lat' : latcoord, 'lon' : loncoord, 'appid' : '1156d71518eb434f16df8c9eed318677'}
    respond = requests.get("http://api.openweathermap.org/data/2.5/weather?", params = finalquery)
    jsondata = respond.json()
    print("\nTemperature: %.1f C\nWind: %.1f m/s" % (jsondata["main"]["temp"]-273.15, jsondata["wind"]["speed"]))
    Dir = direction(jsondata["wind"]["deg"])
    print("Direction: " + Dir)

if x == 2: 
    print("\nEnter city id: ")
    a = input()
    query = {'id': a, 'appid' : '1156d71518eb434f16df8c9eed318677'}
    respond = requests.get("http://api.openweathermap.org/data/2.5/weather?", params = query)
    jsondata = respond.json()
    print("\nTemperature: %.1f C\nWind: %.1f m/s" % (jsondata["main"]["temp"]-273.15, jsondata["wind"]["speed"]))
    Dir = direction(jsondata["wind"]["deg"])
    print("Direction: " + Dir)

if x == 3: 
    print("\nEnter ZIP code: ")
    a = input()
    query = {'zip': a, 'appid' : '1156d71518eb434f16df8c9eed318677'}
    respond = requests.get("http://api.openweathermap.org/data/2.5/weather?", params = query)
    jsondata = respond.json()
    print("\nTemperature: %.1f C\nWind: %.1f m/s" % (jsondata["main"]["temp"]-273.15, jsondata["wind"]["speed"]))
    Dir = direction(jsondata["wind"]["deg"])
    print("Direction: " + Dir)


