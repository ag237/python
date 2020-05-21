import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

samplereal = input('sample or real?: ')
if samplereal == 'sample' : url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
else : url = 'http://py4e-data.dr-chuck.net/comments_476406.xml'

html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)

totalcounts = list()
for t in tree.findall('.//count'):
  totalcounts.append(float(t.text))

print(sum(totalcounts))