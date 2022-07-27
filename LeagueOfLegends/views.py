from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render
from .models import Friend
import requests
# Create your views here.
lolkey = "RGAPI-635969e1-3ad7-4c21-a6a5-d8d9654858af"
region ="euw1"
server= "europe"

def index(request):
    return render(request, 'index.html')


def player(request):

    textplayer = request.GET.get('search')

    response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+textplayer+"?api_key="+lolkey)
    summonerdata = response.json()
    id = summonerdata['id']
    puuid = summonerdata['puuid']
    iconnumber = summonerdata['profileIconId']
    icon = "http://ddragon.leagueoflegends.com/cdn/12.4.1/img/profileicon/"+str(iconnumber)+".png"


    responseinfouser = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+id+"?api_key="+lolkey)
    infouser = responseinfouser.json()
    emblem = "/static/images/emblems/Emblem_"+infouser[0]['tier']+".png"

    responsematch = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"+puuid+"/ids?api_key="+lolkey)
    matchlist = responsematch.json()

    ##responsematchinfo = requests.get("https://europe.api.riotgames.com/lol/match/v5/matches/"+matchlist[0]+"/timeline?api_key="+lolkey)
    ##matchinfo = responsematchinfo.json()

    return render(request, 'player.html',{
        'summoner_name': infouser[0]['summonerName'],
        'tier':infouser[0]['tier'],
        'rank':infouser[0]['rank'],
        'lp':infouser[0]['leaguePoints'],
        'wins':infouser[0]['wins'],
        'losses':infouser[0]['losses'],
        'level':summonerdata['summonerLevel'],
        'icon': icon,
        'emblem': emblem
    })

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def friends(request):
    friends = Friend.objects.all()
    context = {'friends': friends}
    return render(request, 'friends.html', context)