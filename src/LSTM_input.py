from re import findall
from sys import argv
from mido import MidiFile
from mido import Message,MetaMessage
import numpy as np
from keras.utils import to_categorical


num_notes = 128

def init_array(file, key):
    mid=MidiFile(file)
    notes = []
    size = 0
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on':
                notes.append(msg.note)
        del track
    generate_sequences(notes,3)

def generate_sequences(note_array, seq_size):
    LSTM_in = []
    LSTM_out = []

    for i in range(0, len(note_array) - seq_size, 1):
        seq_in = note_array[i:i + seq_size]
        seq_out = note_array[i + seq_size]
        LSTM_in.append(seq_in)
        LSTM_out.append(seq_out)

    n_patterns = len(LSTM_in)

    LSTM_in = np.reshape(LSTM_in, (n_patterns, seq_size, 1))
    LSTM_in = LSTM_in/float(num_notes)
    LSTM_out = to_categorical(LSTM_out, num_classes=num_notes)

    print(LSTM_in)
    print("-----------------------------------------------------")
    print(LSTM_out[0])
