from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    r = requests.get('http://ddragon.leagueoflegends.com/cdn/11.11.1/data/en_US/champion.json')
    data = r.json()
    splashRes = requests.get('http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ornn_0.jpeg')
    art = splashRes.content
    champions = data["data"]
    print(champions["Akali"])
    return render(request, "buildgenerator/index.html", {
        "champions": champions,
        "art": art,
    })