from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    r = requests.get('http://ddragon.leagueoflegends.com/cdn/11.11.1/data/en_US/champion.json')
    data = r.json()
    champions = data["data"]
    print(champions["Akali"])
    return HttpResponse(champions)