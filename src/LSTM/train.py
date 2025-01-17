from re import findall
from sys import argv, path
path.append('../../utils')
from mido import MidiFile
from mido import Message,MetaMessage
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import BatchNormalization as BatchNorm
from tensorflow.keras.callbacks import ModelCheckpoint
from os import listdir, chdir, getcwd, mkdir
from get_notes import get_arr_notes

def init_array(num_notes):
    dir0 = '../dataset/'
    notes = get_arr_notes(dir0)
    return generate_sequences(notes, 100, num_notes)

def generate_sequences(note_array, seq_size, num_notes):
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
    return (LSTM_in, LSTM_out)


def init_lstm_model(LSTM_in, num_notes):
    print('init lstsm model ------------------------------------------------')
    """ create the structure of the neural network """
    model = Sequential()
    model.add(LSTM(
        512,
        input_shape=(LSTM_in.shape[1], LSTM_in.shape[2]),
        recurrent_dropout=0.3,
        return_sequences=True
    ))
    model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3,))
    model.add(LSTM(512))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(BatchNorm())
    model.add(Dropout(0.3))
    model.add(Dense(num_notes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    return model


def train(model, LSTM_in, LSTM_out):
    """ train the neural network """
    filepath = "weights/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
    checkpoint = ModelCheckpoint(
        filepath,
        monitor='loss',
        verbose=0,
        save_best_only=True,
        mode='min'
    )
    callbacks_list = [checkpoint]
    model.fit(LSTM_in, LSTM_out, epochs=50, batch_size=10, callbacks=callbacks_list)
    model.save('/model/lstm_e100_s100.h5')



def train_model():
    num_notes = 128
    print('init array---------------------------------------------')
    network_in, network_out = init_array(num_notes)
    print('train lstm---------------------------------------------')
    train(init_lstm_model(network_in, num_notes), network_in, network_out)

if __name__ == '__main__':
    train_model()
