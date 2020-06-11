from django.shortcuts import render
from django.http import JsonResponse
import requests

ak="mQ3rRVHumsIWrc3gWIcF0iAZtZyaOjo6"

def getCity(request):
    lat=request.GET['lat']
    lng=request.GET['lng']
    url_location = "http://api.map.baidu.com/geocoder/v2/?ak={0}&location={1},{2}&output=json&pois=1".format(ak,lat,lng)
    rq = requests.get(url=url_location)
    try:
        city = rq.json().get("result").get("addressComponent").get("city")
        print(city)
    except:
        city=""
    json={
        "status":0,
        "message":{
            "latitude": lat,
            "longitude": lng,
            "city": city
        }
    }
    print(str(json))
    return JsonResponse(json)

def haversine(lat1, lon1,lat2 , lon2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    url_drive = "http://api.map.baidu.com/routematrix/v2/walking?output=json&origins={0},{1}&destinations={2},{3}&{4}&tactics=11&ak={4}".format(lat1, lon1, lat2, lon2,ak)
    rq=requests.get(url=url_drive)
    distance=rq.json().get("result")[0].get("distance").get("text")
    duration=rq.json().get("result")[0].get("duration").get("text")
    return distance,duration


def getShop(request):
    local_lat=float(request.GET['lat'])
    local_lng=float(request.GET['lng'])
    text="商店"
    radius="10000"
    message=[]
    url = "http://api.map.baidu.com/place/v2/search?query={0}&location={1},{2}&radius={3}&output=json&ak={4}".format(text,local_lat,local_lng,radius,ak)
    rq = requests.get(url=url)
    try:
        for item in rq.json().get("results"):
            lat = item.get("location").get("lat")
            lng = item.get("location").get("lng")
            distance, duration = haversine(local_lat, local_lng, lat, lng)
            message.append({
                "name": item.get("name"),
                "address": item.get("address"),
                "telephone": item.get("telephone", ""),
                "lat": lat,
                "lng": lng,
                "distance": distance,
                "duration": duration
            })
    except:
        message=[]
    json={
        "status":0,
        "message":message
    }
    print (json)
    return JsonResponse(json)

def getCoffee(request):
    local_lat=float(request.GET['lat'])
    local_lng=float(request.GET['lng'])
    text="网吧"
    radius="10000"
    message=[]
    url = "http://api.map.baidu.com/place/v2/search?query={0}&location={1},{2}&radius={3}&output=json&ak={4}".format(text,local_lat,local_lng,radius,ak)
    rq = requests.get(url=url)
    try:
        for item in rq.json().get("results"):
            lat = item.get("location").get("lat")
            lng = item.get("location").get("lng")
            distance, duration = haversine(local_lat, local_lng, lat, lng)
            message.append({
                "name": item.get("name"),
                "address": item.get("address"),
                "telephone": item.get("telephone", ""),
                "lat": lat,
                "lng": lng,
                "distance": distance,
                "duration": duration
            })
    except:
        message=[]
    json={
        "status":0,
        "message":message
    }
    print (json)
    return JsonResponse(json)

def getMore(request):
    local_lat=float(request.GET['lat'])
    local_lng=float(request.GET['lng'])
    local_type = request.GET['type']
    if local_type=="coffee":
        text="网吧"
    else:
        text="超市"
    radius="10000"
    message=[]
    url = "http://api.map.baidu.com/place/v2/search?query={0}&location={1},{2}&radius={3}&output=json&ak={4}".format(text,local_lat,local_lng,radius,ak)
    rq = requests.get(url=url)
    try:
        for item in rq.json().get("results"):
            lat = item.get("location").get("lat")
            lng = item.get("location").get("lng")
            distance, duration = haversine(local_lat, local_lng, lat, lng)
            message.append({
                "name": item.get("name"),
                "address": item.get("address"),
                "telephone": item.get("telephone", ""),
                "lat": lat,
                "lng": lng,
                "distance": distance,
                "duration": duration
            })
    except:
        message=[]
    json={
        "status":0,
        "message":message
    }
    print (json)
    return JsonResponse(json)