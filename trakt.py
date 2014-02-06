__author__ = 'Batuhan BUYUKGUZEL'

"""
-TO-DO List-
-> which tv series will air next week
-> refresh information like every day or every 12 hours etc
-> convert time result utc to utc+2
"""

from datetime import datetime
import hashlib
import urllib.parse
import urllib.request
import json

try:
    file = open("trakt.txt", "r+")
except:
    username = input("What is your username?\n>> ")
    password = hashlib.sha1(input("What is your password?\n>> ").encode('utf-8')).hexdigest()
    file = open("trakt.txt", "w")
    file.write(username+"\n")
    file.write(password+"\n")
    file.close()
else:
    username = file.readline().rstrip('\n')
    password = file.readline().rstrip('\n')
    file.close()


def read_json(url):
    req = urllib.request.urlopen(url).read()
    return json.loads(req.decode('utf-8'))

def time(): # I'm not using this func now. But I may need later.
    url_time = "http://api.trakt.tv/server/time.json/API KEY"
    return datetime.utcfromtimestamp(read_json(url_time)['timestamp'])

def this_week(): # Shows monday to sunday
    url = "http://api.trakt.tv/user/calendar/shows.json/API KEY/%s" % username
    req = urllib.request.urlopen(url).read()
    metro = json.loads(req.decode('utf-8'))

    for i in range(0, len(metro)):
        for j in range(0, len(metro[i]['episodes'])):
            title = metro[i]['episodes'][j]['show']['title']
            season = metro[i]['episodes'][j]['episode']['season']
            episode = metro[i]['episodes'][j]['episode']['number']
            air_date = metro[i]['date']
            air_time = metro[i]['episodes'][j]['show']['air_time_utc']
            print(title + "   (S"+str(season).zfill(2)+"E"+str(episode).zfill(2)+")")
            print("  >> "+air_date+"   "+air_time)

this_week()