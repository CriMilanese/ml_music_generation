import requests
import os
import re

years = ['2018','2017', '2015', '2014', '2013', '2011', '2009', '2008', '2006', '2004', '2002']

def req(urll):
    midi = requests.get(urll)
    #print(str(midi.text))
    tracks = re.findall('2[0-1][0-1][0-9]/[a-zA-Z0-9]*.MID', str(midi.text));
    return tracks

def request_files(names, year):
    if not os.path.exists('midi/'+year):
        os.mkdir('midi/'+year)
    os.chdir('midi/'+year)
    for trk in names:
        response = requests.get('http://www.piano-e-competition.com/MIDIFiles/'+trk)
        with open(trk[5:], 'wb') as fp:
            fp.write(response.content)

for yr in years:
    if not os.path.exists('midi'):
        os.chdir('../../')
    trks = req('http://www.piano-e-competition.com/midi_'+yr+'.asp')
    request_files(trks, yr)
