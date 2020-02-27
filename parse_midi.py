# main functions:
    # parse MIDI file

#from MIDI import MIDIFile
from re import findall
from sys import argv
from mido import MidiFile
from mido import Message
import numpy as np

def parse(file):
    mid=MidiFile(file)
    #c.parse()
    p = []
    notes = []
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on':
                notes.append(msg.note)
        del track
    # del p
    my_dict = {}
    for indx, n in enumerate(notes):
        if indx+1 < len(notes):
            # add each new note to the list and append
            # the following note to the followers list
            if n not in my_dict.keys():
                my_dict[n] = np.zeros(128)
                my_dict[n][notes[indx+1]] = 1
            else:
                my_dict[n][notes[indx+1]] += 1

    for note in my_dict.keys():
        print(note , ': ')
        counter= 0
        for foll in my_dict[note]:
            print(foll, 'for key note ',note,'at counter',counter)
            counter += 1
    del notes
    #return my_dict

parse(argv[1])
