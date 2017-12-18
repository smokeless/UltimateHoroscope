import requests
from bs4 import BeautifulSoup

url = 'https://www.freewillastrology.com/horoscopes/horo-archive.html'


#TODO:
#Pull all of the printer friendly files down
#Trim off the advertising in them
#Sort them by sign



r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
file = 'allTheThings'
rawLinkArray = []

for link in soup.find_all('a', href=True):
    if '..' in link['href'] or 'email' in link['href'] or 'p' not in link['href']:
        pass
    else:
        rawLinkArray.append(url + '/' + link['href'])

#before we loop through all this madness, let's work on one file.
