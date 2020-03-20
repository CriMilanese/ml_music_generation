#function that makes a midi file from the markov_chain generates notes, and stores the midi file
# in the 'generated_MIDI' folder in src -- it gives random name to midi files
from mido import Message, MidiFile, MidiTrack
from os import listdir, chdir, getcwd, mkdir
import random
import string


def generate_midi_name(generated_notes):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))

def playback(generated_notes):
    song_name = generate_midi_name(generated_notes)
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    for notes in generated_notes:
        track.append(Message('note_on', note=notes, velocity=100, time=100))
        track.append(Message('note_off', note=notes, velocity=127, time=100))
    print(getcwd())
    chdir('generated_MIDI')
    mid.save(song_name+'.mid')
