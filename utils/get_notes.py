import mido
from os import listdir, chdir, getcwd, path
import sys

notes = []

def get_arr_notes(dir):
    num = dir[-1:]
    if num.isdigit():
        num = int(num)
        dir0 = dir[:-1]
    elif num == '/':
        num = -1
        dir0 = dir
    for entry in listdir(dir0):
        num -= 1
        if num == 0:
            continue
        if not path.isdir(entry):
            if entry.lower.endswith('.mid') :
                mid=mido.MidiFile(dir0+entry)
                for track in mid.tracks:
                    for msg in track:
                        if msg.type == 'note_on':
                            notes.append(msg.note)
                    del track
        else:
            return get_arr_notes(dir0+entry)
    del num
    return notes
