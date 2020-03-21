# this script is meant to download legit .mid files from the piano e-competition
# database, which contains songs divided by year
# OUTPUT: the script generates the necessary folders to sort songs based on the
# year as they are stored in the website

import requests
import os
import re


def seek_through_filenames(urll):
    midi = requests.get(urll)
    #print(str(midi.text))
    tracks = re.findall('2[0-1][0-1][0-9]/[a-zA-Z0-9]*.MID', str(midi.text));
    return tracks

def request_files(names, year):
    if not os.path.exists('../src/midi/'+year):
        os.mkdir('../src/midi/'+year)
    os.chdir('../src/midi/'+year)
    for trk in names:
        response = requests.get('http://www.piano-e-competition.com/MIDIFiles/'+trk)
        with open(trk[5:], 'wb') as fp:
            fp.write(response.content)

def get_midi_files():
    years = ['2018','2017', '2015', '2014', '2013', '2011', '2009', '2008', '2006', '2004', '2002']
    for yr in years:
        trks = seek_through_filenames('http://www.piano-e-competition.com/midi_'+yr+'.asp')
        request_files(trks, yr)
        os.chdir('../')


if __name__ == '__main__':
    get_midi_files()
