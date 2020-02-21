# main functions:
    # parse MIDI file

from MIDI import MIDIFile
import re


def parse(file):
    c=MIDIFile(file)
    c.parse()
    for idx, track in enumerate(c):
        track.parse()
        print(f'Track {idx}:')
        p = re.findall('NOTE_ON\[[0-9]\] [A-Z][0-9] ON',str(track))

    notes = []
    for indx, g in enumerate(p):
        g = g[-5]+g[-4]
        notes.append(g)

    inner_list = []
    my_dict = {}
    for indx, n in enumerate(notes):
        if n != notes[-1]:
            # add each new note to the list and append
            # the following note to the followers list
            if n not in my_dict:
                my_dict[n] = inner_list
                my_dict[n].append((notes[indx+1], 1))
                continue
            contained = False
            counter = 0
            for nt, occ in my_dict[n]:
                # if follower note is present, add occurrance
                if notes[indx+1] == nt:
                    contained = True
                    my_dict[n][counter] = (notes[indx+1], occ+1)
                counter += 1
            del counter
            if not contained:
                # for each follower note, add if not present
                 my_dict[n].append((notes[indx+1], 1))

    # for note in my_dict:
    #     print(note + ': ')
    #     for foll in my_dict[note]:
    #         print('\t' + foll[0] + ' appears: ' + str(foll[1]) + ' times')
    del notes
    del inner_list
    return my_dict
