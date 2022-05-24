
from django.shortcuts import render
#from example.models import Book
import requests
import json
from django.contrib.auth.decorators import login_required


@login_required
def weather(request): # for sending weather data of 10 city according to page no
    #api_id of openweather api
    appid = "4a1f8a61b74546825af1e0be106e797b"
    #page no for pag
    page=1
    l=[]
    try:
        page=request.GET["page"]

    except:
        pass


    cities=['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Kolkata', 'Chennai', 'Surat', 'Pune', 'Jaipur', 'Lucknow', 'Indore', 'Thane', 'Bhopal', 'Patna', 'Vadodara', 'Ludhiana', 'Agra', 'Nashik', 'Rajkot', 'Varanasi', 'Srinagar', 'Dhanbad', 'Amritsar', 'Jodhpur', 'Raipur', 'Kota', 'Guwahati', 'Gurgaon', 'Kochi']
    cities1=cities[:10]
    count = 0
    if int(page)==1:
        cities1=cities[:10]
        count=0
    elif int(page)==2:
        cities1=cities[10:20]
        count=10
    elif int(page)==3:
        cities1=cities[20:30]
        count=20



    for city in cities1:
        url = "https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid, city)
        try:
            response = requests.get(url)
            code = response.status_code
            if code != 200:

                result = city+"!!!Something went wrong or You entered the wrong city name!!!"
                print(result)
            else:
                #weatherDetail=CityWeatherDetails()
                d = {}
                jsondata = json.loads(response.text)
                #print(jsondata["name"],jsondata["main"]["temp"])
                count+=1
                d["sno"]=count
                d["name"] =jsondata["name"]
                d["temp"]=jsondata["main"]["temp"]
                #print(weatherDetail.name,weatherDetail.temp)
                d["max_temp"]=jsondata["main"]["temp_min"]
                d["min_temp"]=jsondata["main"]["temp_max"]
                d["humidity"]=jsondata["main"]["humidity"]
                d["pressure"]=jsondata["main"]["pressure"]
                d["icon"]=jsondata["weather"][0]["icon"]
                d["sunrise"]=jsondata["sys"]["sunrise"]
                d["sunset"]=jsondata["sys"]["sunset"]
                d["main"]=jsondata["weather"][0]["main"]
                d["windspeed"]=jsondata["wind"]["speed"]
                print(d)
                # temp = jsondata["main"]["temp"]
                # humidity = jsondata["main"]["humidity"]
                # result = ""
                #print(temp,humidity)
                #print(weatherDetail)
                l.append(d)
        except:
            result = "!!!Something went wrong or You entered the wrong city name!!!"
    x=l[:10]
    print(l)



    return render(request, "Weather.html", {"data": x,"page":page,"list":l})
#weather()