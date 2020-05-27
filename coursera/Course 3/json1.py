import json
import urllib.request, urllib.parse, urllib.error

samplereal = input('sample or real?: ')
if samplereal == 'sample' : url = 'http://py4e-data.dr-chuck.net/comments_42.json'
else : url = 'http://py4e-data.dr-chuck.net/comments_476407.json'

data = urllib.request.urlopen(url).read().decode()
jdata = json.loads(data)

totalcounts = list()
for user in jdata['comments']:
  totalcounts.append(float(user['count']))

print(sum(totalcounts))