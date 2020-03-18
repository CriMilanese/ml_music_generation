from LSTM import *
from tensorflow.keras.utils import to_categorical, Sequence
import os
import mido
import numpy as np

# I am trying to test the LSTM model from the example I linked
# in the Trello board

dir = '../midi/2018/'
notes = []

for file in os.listdir(dir):
    # but I take only one song
    if file.endswith('18.MID'):
        md = mido.MidiFile(dir+file)
        for msg in md:
            if msg.type == 'note_on':
                # appending each note to a list
                notes.append(msg.note)

n_vocab = 128
network_input = []
network_output = []
seq_len = 100

for i in range(0, len(notes)-seq_len, 1):
    # tmp = notes[i:i+seq_len]
    network_input.append([notes[i:i+seq_len]])
    network_output.append(notes[i+seq_len])

#reshaping to conform to lstm
network_input = np.reshape(network_input, (len(network_input), seq_len,1))
# one-hot encode the output labels
network_output = to_categorical(network_output, num_classes=n_vocab)
#normalize
network_input = network_input/n_vocab

model = create_network(network_input, n_vocab)

# save checkpoints so we can actually
# filepath = "models/weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5"
# checkpoint = ModelCheckpoint(
#     filepath, monitor='loss',
#     verbose=0,
#     save_best_only=True,
#     mode='min'
# )
# callbacks_list = [checkpoint]

epochs_t = 30
print(model.summary())
model.fit(network_input, network_output, epochs=epochs_t, batch_size=128)
model.save('models/my_model_{}.h5'.format(epochs_t))
print('we fitted the model to our data')
del model
