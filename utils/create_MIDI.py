# function that makes a midi file from any array of integers between 1 and 128
# and stores it in the 'generated_MIDI' folder in src/[model]/
# it gives random name to midi files
# it can also be used as a stand-alone utility to be fed with npy files as arg
from mido import Message, MidiFile, MidiTrack
from os import listdir, chdir, getcwd, mkdir
import random
import string
from sys import argv

def generate_midi_name(generated_notes):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))

def create_midi(generated_notes, model_name):
    if generated_notes == []:
        return
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    for notes in generated_notes:
        track.append(Message('note_on', note=notes, velocity=100, time=100))
        track.append(Message('note_off', note=notes, velocity=127, time=100))
    store(mid, model_name)

def store(mido_MIDI, model_name):
    if not os.path.exists('../src/{}'.format(model_name)):
        mkdir('../src/{}'.format(model_name))
        mkdir('../src/{}/generated_MIDI'.format(model_name))
    song_name = generate_midi_name(generated_notes)
    chdir('../src/{}/generated_MIDI'.format(model_name))
    mido_MIDI.save(song_name+'.mid')

if __name__ == '__main__':
    if argv[1] == None:
        create_midi([], '')
    else:
        create_midi(argv[1], argv[2])
