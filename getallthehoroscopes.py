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
for link in soup.find_all('a', href=True):
    print(url+'/'+link['href'])

    #with open(file, 'w') as myFile:
    #    myFile.write(req.text)
    #print(link['href'])