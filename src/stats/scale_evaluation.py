from os import listdir, chdir, getcwd, mkdir
from mido import MidiFile

def parse(file):
    mid = MidiFile(file)
    notes = []
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on':
                notes.append(msg.note)
        del track

    return notes

def init_array():
    c_maj_base = [0, 2, 4, 5, 7, 9, 11]
    e_maj_base = [4, 6, 8, 9, 11, 1, 2]
    c_maj = []
    for i in c_maj_base:
        for x in range(10):
            hex_val = i + (x * 12)
            if(hex_val <= 127):
                c_maj.append(hex_val)

    return c_maj

def gen_metric(file):
    counter = 0
    for note in file:
        if note in init_array():
            counter = counter + 1

    note_percentage = (counter / len(file)) * 100

    return note_percentage



chdir('Data')
print(gen_metric(parse('new_song.mid')))
