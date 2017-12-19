import markovify

def selectFile(zodiacSign: str)->str:
    '''Figure out what we're going to use as our input'''
    txt = ''
    with open(zodiacSign, 'r') as myFile:
        txt = myFile.read()
    return txt

def generateScope(seed: str)->str:
    text_model = markovify.Text(seed)
    lines = ''
    for i in range(3): #how many lines we generate for this horoscope.
        lines += text_model.make_sentence(max_overlap_ratio=100)
        lines += '\n'
    lines = lines.split('.')
    for i in range(0, (len(lines)-1)):
        if 'Audio' in lines[i] or 'AUDIO' in lines[i] or 'audio' in lines[i]:
            del lines[i]
    lines = '.'.join(lines)
    lines = lines.strip()
    if len(lines) == 0:
        generateScope(seed)
    return lines


def generateAllScope():
    signs = ['Aquarius', 'Aries', 'Cancer', 'Capricorn', 'Gemini',
             'Leo', 'Libra', 'Pisces', 'Sagittarius', 'Scorpio',
             'Taurus', 'Virgo']
    for e in signs:
        txt        = selectFile(e)
        horoscope  = generateScope(txt)
        print(e, 'your horoscope is:')
        print(horoscope, '\n')

generateAllScope()