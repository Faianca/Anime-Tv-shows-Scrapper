__author__ = 'jmeireles'

import dryscrape
import re
import requests
import bs4
import urllib

regex = '(?<=file:\s")http://[^\s"]+.(?:mp4|mpg|avi|flv)'
'''
url = 'http://gorillavid.in/embed-sx5p5f4cbgm1-650x400.html'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text)

text = soup.get_text()
regex = urllib.unquote(regex)
url = re.search(regex, str(text))
print urllib.unquote(url.group()).decode('utf8')

'''


url = "http://embed.movshare.net/embed.php?v=ba47de88ca2a2&width=655&height=362"

session = dryscrape.Session()
session.visit(url)
response = session.body()
soup = bs4.BeautifulSoup(response)
print soup.text
movshareDomain = re.search('(?<=flashvars.domain=)"?(?P<match>[^";]+)', soup.text)
print urllib.unquote(movshareDomain.group("match")).decode('utf8')
movshareFile = re.search('(?<=flashvars.file=)"?(?P<match>[^";]+)', soup.text)
print urllib.unquote(movshareFile.group("match")).decode('utf8')
movshareKey = re.search('(?<=flashvars.filekey=)"?(?P<match>[^";]+)', soup.text)
print urllib.unquote(movshareKey.group("match")).decode('utf8')
movshareCID = re.search('(?<=flashvars.cid=)"?(?P<match>[^";]+)', soup.text)
print urllib.unquote(movshareCID.group("match")).decode('utf8')

'''
movshareVideoURL = getMyContent(movshareDomain + "/api/player.api.php?cid=" + movshareCID + "&file=" +movshareFile + "&key=" + movshareKey, 'TEXT', false);
movshareVideoURL = decodeURIComponent(movshareVideoURL.match('[domain|url]=(.*?)&')[1]);
'''