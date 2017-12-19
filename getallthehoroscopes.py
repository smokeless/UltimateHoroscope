import requests
from bs4 import BeautifulSoup
'''
This isn't really part of the project. 
But if I use other sites as well I don't want to
dl and parse everything by hand. Nor do I want to DL/parse
this stuff with bins to pipes.
'''


#TODO:
#Pull all of the printer friendly files down
#Trim off the advertising in them
#Sort them by sign


def getFreeWill():
    '''This pulls down the freewillastro archives to seed
       the Markov.
    '''
    url  = 'https://www.freewillastrology.com/horoscopes/horo-archive.html'
    url2 = 'https://www.freewillastrology.com/horoscopes/'  # links come from first url
                                                            # this is where they need to
                                                            # be appended.
    r            = requests.get(url)
    soup         = BeautifulSoup(r.text,'html.parser')
    file         = 'free_will_astro.txt'
    rawLinkArray = []

    for link in soup.find_all('a', href=True):
        if '..' in link['href'] or 'email' in link['href'] or 'p' not in link['href']:
            pass
        else:
            rawLinkArray.append(url2 + link['href'])


    req         = requests.get(rawLinkArray[0])
    moreSoup    = BeautifulSoup(req.text, 'html.parser')
    workingText = moreSoup.text
    cleanText   = ''
    for line in workingText.splitlines():
        if line == '*':
            pass
        else:
            cleanText += '\n'
            cleanText += line
    print(cleanText)


getFreeWill()