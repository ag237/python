import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

counter = 0
pcounter = 1

url = input('Enter url: ')
position = float(input('Enter position: '))
count = float(input('Enter count: '))


while counter < count:
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  for tag in tags:
    if pcounter == position:
      url = tag.get('href', None)
      print(url)
      pcounter = 1
      break
    else: pcounter = pcounter + 1
  counter = counter + 1