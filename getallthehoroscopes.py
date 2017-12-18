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
url2 = 'https://www.freewillastrology.com/horoscopes/' #links come from first url
                                                       #this is where they need to
                                                       #be appended. Probably a
                                                       #better way to do this.

for link in soup.find_all('a', href=True):
    if '..' in link['href'] or 'email' in link['href'] or 'p' not in link['href']:
        pass
    else:
        rawLinkArray.append(url2 + link['href'])
        print(url2 + link['href'])

#testing
req = requests.get(rawLinkArray[0])
moreSoup = BeautifulSoup(req.text, 'html.parser')
print(moreSoup.text)

