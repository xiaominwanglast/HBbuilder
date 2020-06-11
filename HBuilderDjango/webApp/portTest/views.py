from django.shortcuts import render
from django.http.response import JsonResponse

def renderIndex(request):
    return render(request,"/")


def showIndex(request):
    json={
        "status":200,
        "message":True,
        "data":{
            "title":"首页","size":"30"
        }
    }
    return JsonResponse(json)
# Create your views here.
