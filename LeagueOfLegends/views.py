from asyncio.windows_events import NULL
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Friend
from django.contrib import messages

import requests
# Create your views here.
lolkey = "RGAPI-33571076-2814-4781-b986-baeefcdafa8a"
region ="euw1"
server= "europe"

def index(request):
    return render(request, 'index.html')

def player(request):
    textplayer = request.GET.get('search')
    return getplayer(request,textplayer)

def getplayer(request, pk):
    if pk is not None:
        textplayer = pk
    else:
        textplayer = request.GET.get('search')
    try:
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
    except:
        messages.info(request,'Not summoner with this name this season')
        return redirect('/')
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


def friends(request):
    friends = Friend.objects.all()
    context = {'friends': friends}
    return render(request, 'friends.html', context)