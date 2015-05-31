#-------------------------------------------------------------------------------
# Name:        imdb-lookup
# Purpose:
#
# Author:      manoj mj
#
# Created:
# Copyright:   (c) www.manojmj.com
# Licence:
#-------------------------------------------------------------------------------

import urllib
import json
import webbrowser

import sys

def finder(name):
    replace = [".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}"
    "x264","720p","StyLishSaLH (StyLish Release)","DvDScr","MP3","HDRip","WebRip",
    "ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio","EngHindiIndonesian",
    "385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub","AQOS",
    "ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE",
    "BRRIP","XVID","AbSurdiTy","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
    "Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    "GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","com",
    "1080p","1080","SecretMyth","Kingdom","Release","RISES","DvDrip","ViP3R","RISES","BiDA","READNFO",
    "HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED","Series","ExtraTorrent","DVDRIP","~",
    "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264","phrax","ENG","TODE","LiNE",
    "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP","MoH","MP4","BadMeetsEvil",
    "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61","NL","EE","Rel","NL",
    "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB","7o9",
    "Exclusive","171","DiDee","v2"

    ]
    year=0
    for y in range(1900,2014):
        if str(y) in name:
            name = name.replace(str(y)," ")
            year = y
            break
    for value in replace:
        name = name.replace(value," ")

    name = name.strip();

    if year!=0:
        url = "http://www.omdbapi.com/?t="+name+"&y="+str(year)
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        if jsonvalues["Response"]=="True":
            movieurl = "www.imdb.com/title/" + jsonvalues['imdbID']
            webbrowser.open_new_tab(movieurl)

    else:
        url = "http://www.omdbapi.com/?t="+name
        response = urllib.urlopen(url).read()
        jsonvalues = json.loads(response)
        if jsonvalues["Response"]=="True":
            movieurl = "www.imdb.com/title/" + jsonvalues['imdbID']
            webbrowser.open_new_tab(movieurl)

file = sys.argv[1].split("\\")[-1]
finder(file)
