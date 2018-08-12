import urllib.request as ur
import json
import webbrowser

import sys

#list of words, we need to remove to get the clean movie name to search in movie database
def finder(name):
    replace = ["E SuB xRG",".avi","1.4","5.1","-","DVDRip","BRRip","XviD","1CDRip","aXXo","[","]","(",")","{","}","{{","}}",
    		"x264","720p","DvDScr","MP3","HDRip","WebRip","ETRG","YIFY","StyLishSaLH","StyLish Release","TrippleAudio",
    		"EngHindiIndonesian","385MB","CooL GuY","a2zRG","x264","Hindi","AAC","AC3","MP3"," R6","HDRip","H264","ESub",
		"AQOS","ALLiANCE","UNRATED","ExtraTorrentRG","BrRip","mkv","mpg","DiAMOND","UsaBitcom","AMIABLE","BRRIP","XVID",
		"AbSurdiTy","DvD","mp3","MPEG4","CRYS","DVDRiP","TASTE","BluRay","HR","COCAIN","_",".","BestDivX","MAXSPEED",
		"mediafiremoviez","Eng","500MB","FXG","Ac3","Feel","Subs","S4A","BDRip","FTW","Xvid","Noir","1337x","ReVoTT",
    		"GlowGaze","mp4","Unrated","hdrip","ARCHiViST","TheWretched","www","torrentfive","1080p","201 080p","1080",
		"WEB DL","JYK","SecretMyth","Kingdom","Release","RISES","DvDrip","eXceSs","ViP3R","RISES","BiDA","READNFO",
		"lish","NimitMak","SilverRG","sujaidr","HELLRAZ0R","tots","BeStDivX","UsaBit","FASM","NeroZ","576p","LiMiTED",
		"Series","ExtraTorrent","DVDRIP","~", "BRRiP","699MB","700MB","greenbud","B89","480p","AMX","007","DVDrip","h264",
		"phrax","ENG","TODE","LiNE", "XVid","sC0rp","PTpower","OSCARS","DXVA","MXMG","3LT0N","TiTAN","4PlayHD","HQ","HDRiP",
		"MoH","MP4","BadMeetsEvil", "XViD","3Li","PTpOWeR","3D","HSBS","CC","RiPS","WEBRip","R5","PSiG","'GokU61","GB","GokU61",
		"NL","EE","NL", "PSEUDO","DVD","Rip","NeRoZ","EXTENDED","DVDScr","DVDSCR","xvid","WarrLord","SCREAM","MERRY","XMAS","iMB",
		"7o9","Exclusive","171","DiDee","v2","Scr","SaM","MOV","BRrip","CharmeLeon","Silver RG","1xCD","DDR","1CD","X264",
		"ExtraTorrenRG","Srkfan","UNiQUE","Dvd","Dual Audio","crazy torrent","Blackjesus","RIP","NEO","Mr  KickASS","Mr KickASS",
		"MicroStar RG","Spidy","PRiSTiNE","HD","Ganool","TS","BiTo","ARiGOLD","rip","Rets","teh","ChivveZ","song4",
		"playXD","LIMITED","600MB","700MB","900MB","350MB","375MB","380MB","395MB","2015","2014","Manudil","P2PDL","juggs"
		,"RLSM","WiLDFYRE","prisak","HKRG","FANTASTiC","MZON3","BlackStaticRG","Subtitles","+","PDvD","MyDownloadCity","GooN","Ali Baloch",
		"dvd","- ","DUB","BDRIP","6CH","KIKS","HC", "EVO","Maxillion","BHATTI87","2 0","lish","Lokioddin","PimpRG","AG","BUZZccd","WBRG",
		"GECKOS","H 264","TheFalcon", "PLAYNOW","DUBBED", "OCW","mSD","AliBaloch","Mediafiremoviez","BlueRay","EVO","IceBane","RyD3R",
		"Zwartboek","CODY","MiCRO","Dual","R@J@T","cam","Demonuk", "NIKONRG","AbhinavRocks","HKRG","FLAWL3SS","Jalucian","DTS","DVDRip",
		"XviD","MAXSPEED","www.torentz.3xforum.ro","iTALiAN","MD","Dual","TrTd", "TeaM","KiNGDOM","KumaR","UNCUT","BHATTI87","P2PDL",
		"Antitrust","26K","Dias","Rus  Junoon","RARBG","PA","GreatMagician","4 G","ChattChitto","RG",
		"BD  D","6ch","Tornster","Atlas47","480P","DUAL AUDIO","HINDI","PRINCEOFDHEMP","DD","EN","SCR","IMAX EDITION","COD","cam","1080P",
   		 "AraGon","BD","6Chn Cody's","YTS.AG","KickASS","DUBBED","Mediafiremoviez.com","mediafiremoviez.com"
	      ]
    year=0
    for y in range(1900,2014):
        if str(y) in name:
            name = name.replace(str(y)," ")
            year = y
            break
    #if movie name contains any value from the replace[] list, replace it with space        
    for value in replace:
        name = name.replace(value," ")

    name = name.strip();
    
    #"apikey=9b925aaa" is set for now, you can create the key from http://www.omdbapi.com/apikey.aspx and change it
    if year!=0:
        url = "http://www.omdbapi.com/?t="+name+"&y="+str(year)+"&apikey=9b925aaa"
        print (url)
        response = ur.urlopen(url).read() #get the response from API
        jsonvalues = json.loads(response) #load the json response
        if jsonvalues["Response"]=="True":
            movieurl = "www.imdb.com/title/" + jsonvalues['imdbID'] #extract imdbID from json response and open the imdb url with imdbID instead of name of the movie
            webbrowser.open_new_tab(movieurl)
    else:
        url = "http://www.omdbapi.com/?t="+name+"&apikey=9b925aaa"
        response = ur.urlopen(url).read()
        jsonvalues = json.loads(response)
        if jsonvalues["Response"]=="True":
            movieurl = "www.imdb.com/title/" + jsonvalues['imdbID']
            webbrowser.open_new_tab(movieurl)

file = sys.argv[1].split("\\")[-1]
finder(file)
