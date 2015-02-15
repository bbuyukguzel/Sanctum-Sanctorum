__author__ = 'Batuhan BUYUKGUZEL'

import urllib.parse
import urllib.request
import json
from datetime import datetime


class TimestampToGMT:
    def ts_date(self):
        return str(datetime.fromtimestamp(int(self)).strftime('%Y-%m-%d %H:%M:%S'))
    def ts_day(self):
        return str(datetime.fromtimestamp(int(self)).strftime('%A'))
    def ts_hour_12(self):
        return str(datetime.fromtimestamp(int(self)).strftime('%H:%M%p'))
    def ts_hour(self):
        return datetime.fromtimestamp(int(self)).strftime('%H')
    def ts_min(self):
        return datetime.fromtimestamp(int(self)).strftime('%M')
    def ts_hour_min(self):
        return datetime.fromtimestamp(int(self)).strftime('%H:%M')


def read_json(url):
    req = urllib.request.urlopen(url).read()
    return json.loads(req.decode('utf-8'))


def find_location(adress):
    adress = adress.replace(' ', '+')
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % adress
    data = read_json(url)
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    return (lat, lng)


def show_weekly():
    data = read_json(url)
    for i in range(0, 6):
        difference = int(data['daily']['data'][i]['temperatureMax'] - int(data['daily']['data'][i]['temperatureMin']))
        min = str(int(data['daily']['data'][i]['temperatureMin'])) + C
        max = str(int(data['daily']['data'][i]['temperatureMax'])) + C
        time = TimestampToGMT.ts_day(data['daily']['data'][i]['time'])[:3]
        summary = data['daily']['data'][i]['summary']
        #print("%20s%20s%20s%20s%20s") % (time,summary,min,(difference)*"-",max)
        print(time, summary.ljust(35), min, ((difference) * "-").ljust(10), max)


def show_today():
    data = read_json(url)
    temperatureMin = str(int(data['daily']['data'][0]['temperatureMin'])) + C
    temperatureMinTime = TimestampToGMT.ts_hour_12(data['daily']['data'][0]['temperatureMinTime'])
    temperatureMax = str(int(data['daily']['data'][0]['temperatureMax'])) + C
    temperatureMaxTime = TimestampToGMT.ts_hour_12(data['daily']['data'][0]['temperatureMaxTime'])
    sunrise = TimestampToGMT.ts_hour_12(data['daily']['data'][0]['sunriseTime'])
    sunset = TimestampToGMT.ts_hour_12(data['daily']['data'][0]['sunsetTime'])
    print("LOW: " + temperatureMin + " at " + temperatureMinTime)
    print("HIGH: " + temperatureMax + " at " + temperatureMaxTime)


adress = "Kenan evren bulvari,adana" #adress
APIKEY = "YOUR API KEY HERE"
LATITUDE = find_location(adress)[0]
LONGITUDE = find_location(adress)[1]
PARAMETER = "?units=si" #convert to SI units
url = "https://api.forecast.io/forecast/%s/%s,%s%s" % (APIKEY, LATITUDE, LONGITUDE, PARAMETER)
C = u'\u00b0'

show_today()
