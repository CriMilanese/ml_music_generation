from tensorflow.keras.models import *
import numpy as np
import os
import mido
import pickle

model = load_model('models/my_model_30.h5')
dir = '../midi/2018'
notes = []
seq_len = 100
net_in = []

for file in os.listdir(dir):
    # but I take only one song
    if file.endswith('oS15.MID'):
        md = mido.MidiFile(dir+'/'+file)
        for msg in md:
            if msg.type == 'note_on':
                # appending each note to a list
                notes.append(msg.note)

for i in range(0, len(notes)-seq_len, 1):
    net_in.append([notes[i:i+seq_len]])
#reshaping to conform to lstm
net_in = np.reshape(net_in, (len(net_in), seq_len, 1))
net_in = net_in / 90.0
start = np.random.randint(0, len(net_in)-1)
pattern = net_in[start]
# print(pattern)
result = []
len_sequence = 50

for i in range(len_sequence):
        print('prediction number {}'.format(i))
        # print(pattern.shape)
        pred_in = np.reshape(pattern, (1, len(pattern), 1))
        # pred_in = pred_in/float(90)
        pred_out = model.predict(pred_in, verbose=0)
        print(pred_out)
        indx = np.argmax(pred_out)
        print('index found is: ', indx)
        # print('pattern length after argmax is ', len(pattern))
        result.append(indx)
        pattern = np.append(pattern, indx)
        pattern = pattern[1:len(pattern)]
        # print('pattern length after append is ', len(pattern))

print('result content: ', result)
with open('result_{}.pickle'.format(len_sequence), 'wb') as handle:
    pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
handle.close()
