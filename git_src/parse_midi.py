# main functions:
    # parse MIDI file

#from MIDI import MIDIFile
from re import findall
from sys import argv
from mido import MidiFile
from mido import Message,MetaMessage
import numpy as np
from markov_chain import n_grams_frequency

def check(file):
    mid = MidiFile(file)
    #for track in mid.tracks:
    counter = 0
    for msg in mid.tracks[0]:
        counter +=1
        if msg.type == 'time_signature':
            print(msg)
            #print(meta)

            #if msg.type == 'note_on':

                #print(msg)

def normalise(input_key, note_prog):
    notes = [['Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D',
            'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#'],
            [0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 11, 0]]

    const_key_val = notes[1][5]
    const_key = notes[0][5]

    for i in range(len(notes[0])):
        if(notes[0][i] == input_key):
            step_diff = const_key_val - notes[1][i]
        else:
            return note_prog

    for x in range(len(note_prog)):
        note_prog[x] = note_prog[x] + step_diff

    return note_prog


def parse(file, key):
    mid=MidiFile(file)
    notes = []
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on':
                notes.append(msg.note)
        del track
    n_grams_frequency(notes)
    if(key == 'E major'):
        notes = normalise("E", notes)
    if(key == 'F major'):
        notes = normalise("F", notes)
    if(key == 'G major'):
        notes = normalise("G", notes)

    my_dict = {}
    for indx, n in enumerate(notes):
        if indx+1 < len(notes):
            # add each new note to the list and append
            # the following note to the followers list
            if n not in my_dict.keys():
                my_dict[n] = np.zeros(128, dtype= int)
                my_dict[n][notes[indx+1]] = 1
            else:
                my_dict[n][notes[indx+1]] += 1

    for note in my_dict.keys():
        #print(note , ': ')
        counter= 0
        for foll in my_dict[note]:
            #if foll != 0.0:
                #print(foll, 'for key note ',note,'at counter',counter)
            counter += 1
    del notes
    return my_dict
#parse(argv[1])
#check(argv[1])
