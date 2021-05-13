from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import requests
import json

# Create your views here.
url = "https://bookstore-restapi-nodejs.herokuapp.com"

def index(request):
    response = requests.get(url+"/book")
    decoded_json = response.json()["books"]
    list = []
    for book in decoded_json:
        temp = {}
        temp["name"] = book["name"]
        temp["price"] = book["price"]
        temp["author"] = book["Author"]["firstname"] + book["Author"]["lastname"]
        temp["category"] = []
        temp["image"] =book["Image"]
        for category in book["Categories"]:
            temp["category"].append(category["name"])
        list.append(temp)
    return render(request, "index.html", {"list": list})
def signin(request):
    if(request.method=="POST"):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        account = {"username": username, "password": password}
        r = requests.post(url=url+"/login", json=account)
        print(r.json())
        return render(request,"signin.html")
    return render(request,"signin.html")
