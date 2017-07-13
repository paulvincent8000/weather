#Pull weather data for yesterday

#Set Country and City
ctry = 'CH'
cty = 'Zurich'

#No changes below this point

# -*- coding: utf-8 -*-
import urllib2
import json
import datetime
y  = datetime.date.today() + datetime.timedelta(days=-1)
dt = '{:{dfmt}}'.format(y, dfmt='%Y%m%d')
#print (dt)

#Build url with date from yesterday
url1 = 'http://api.wunderground.com/api/dc5687058ecdd725/history_'
url2 = '/q/CH/Zurich.json'
url = url1 + dt + url2
#print(url)

#Read JSON string
f = urllib2.urlopen(url)
json_string = f.read()
#print json_string

#Output to JSON file
with open('weather.json', 'wb') as hi_file:
  hi_file.write(json_string)

f.close()

#add comment to branch paul
