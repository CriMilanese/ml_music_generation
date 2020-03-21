# usage
#   $ python3 predict.py [.h5 file]

# loads the model, samples a song from the dataset and tries to create a sequence
# to label generation

import sys
sys.path.append('../../utils')
from tensorflow.keras.models import *
import numpy as np
import os
import mido
import pickle
from manage_pickles import savePk
from get_notes import get_arr_notes

# def generate():
#
dir = '../dataset/C major/3'
notes = []
seq_len = 100
net_in = []

notes = get_arr_notes(dir)
print(len(notes))
for i in range(0, len(notes)-seq_len, 1):
    net_in.append([notes[i:i+seq_len]])
print(len(net_in[0]))
#reshaping to conform to lstm
net_in = np.reshape(net_in, (len(net_in), seq_len, 1))
net_in = net_in / 128

# feeds the model from a random point along the song
start = np.random.randint(0, len(net_in)-1)
pattern = net_in[start]
# print(pattern)
result = []

model = load_model('models/mdl_CM_epochs50.h5')
for i in range(seq_len):
        print('prediction number {}'.format(i))
        pred_in = np.reshape(pattern, (1, len(pattern), 1))
        pred_in = pred_in/float(128)
        pred_out = model.predict(pred_in, verbose=0)
        indx = np.argmax(pred_out)
        print('index found is: ', indx)
        # print('pattern length after argmax is ', len(pattern))
        result.append(indx)
        pattern = np.append(pattern, indx)
        pattern = pattern[1:len(pattern)]
        # print('pattern length after append is ', len(pattern))

print('result content: ', result)
savePk(pred_out, '../pickles/result_{}'.format(seq_len))
