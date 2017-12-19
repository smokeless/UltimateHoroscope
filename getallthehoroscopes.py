import requests
from bs4 import BeautifulSoup
'''
This isn't really part of the project. 
But if I use other sites as well I don't want to
dl and parse everything by hand. Nor do I want to DL/parse
this stuff with bins to pipes.
'''

def writeToFile(fileName: str, txt):
    '''TODO Writes to a file, for now prints to test logic.'''
    print('*' * 10, 'writing to:', fileName )
    print('*' * 10, 'done writing:', fileName, '*' * 10)
    with open(fileName, 'a') as myFile:
        myFile.write(txt)

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
    rawLinkArray = []

    for link in soup.find_all('a', href=True):
        if '..' in link['href'] or 'email' in link['href'] or 'p' not in link['href']:
            pass
        else:
            rawLinkArray.append(url2 + link['href'])

    for i in rawLinkArray:
        req         = requests.get(i)
        moreSoup    = BeautifulSoup(req.text, 'html.parser')
        workingText = moreSoup.text
    #logic should be like:
    #parse in the line, if the line contains a sign
    #continue to parse in lines until an asterix is
    #hit. Don't add lines after the * until sign is
    #hit.
        appendLinesOn = False
    #maybe refactor this out.
    #signs = ['Aries', 'Taurus', 'Gemini',
    #         'Cancer', 'Leo', 'Virgo',
    #         'Libra', 'Scorpio', 'Sagittarius',
    #         'Capricorn', 'Aquarius', 'Pisces']

        currentSign = ''
        signText = {'Aries':'', 'Taurus':'', 'Gemini':'',
                    'Cancer':'', 'Leo':'', 'Virgo':'',
                    'Libra':'', 'Scorpio':'', 'Sagittarius':'',
                    'Capricorn':'', 'Aquarius':'', 'Pisces':''}
        for line in workingText.splitlines():
            if appendLinesOn == False:
                for i in signText:
                    if i in line:
                        appendLinesOn = True
                        currentSign = i
            if appendLinesOn and '*' == line:
                appendLinesOn = False

            if appendLinesOn:
                signText[currentSign] += line
                signText[currentSign] += '\n'

        for key,value in signText.items():
            writeToFile(key, value)





getFreeWill()