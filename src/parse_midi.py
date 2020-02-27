# main functions:
    # parse MIDI file

from MIDI import MIDIFile
from re import findall
from sys import argv

def parse(file):
    c=MIDIFile(file)
    c.parse()
    p = []
    for track in c:
        track.parse()
        p = findall('NOTE_ON\[[0-9]\] [A-Z][0-9] ON',str(track))
        del track
    notes = []
    for g in p:
        g = g[-5]+g[-4]
        notes.append(g)
    del p
    my_dict = {}
    for indx, n in enumerate(notes):
        if indx+1 < len(notes):
            # add each new note to the list and append
            # the following note to the followers list
            if n not in my_dict.keys():
                my_dict[n] = []
                my_dict[n].append((notes[indx+1], 1))
                continue
            contained = False
            # counter = 0
            for ind, (nt, occ) in enumerate(my_dict[n]):
                # if follower note is present, add occurrance
                if notes[indx+1] == nt:
                    contained = True
                    my_dict[n][ind] = (notes[indx+1], occ+1)
                # counter += 1
            # del counter
            if not contained:
                # for each follower note, add if not present
                my_dict[n].append((notes[indx+1], 1))

    # for note in my_dict:
    #     print(note + ': ')
    #     for foll in my_dict[note]:
    #         print('\t' + foll[0] + ' appears: ' + str(foll[1]) + ' times')
    del notes
    return my_dict

# parse(argv[1])
