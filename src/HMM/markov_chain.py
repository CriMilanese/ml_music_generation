#from dict_to_df import option_df
import pandas as pd
from random import randint,random
import numpy as np
from mido import Message, MidiFile, MidiTrack
from create_MIDI import create_midi

##option_df- creates a dictionary and for each note stores  a list of tuples containing the
#the next note and its probability, this function will be used for the function predict_next_note
def option_df(prob_df):
    note_option = {}
    for key,row in prob_df.iterrows():
        temp_array= list()
        for el in row.iteritems():
            if el[1] > 0:
                temp_array.append(tuple((el[0],el[1])))
        temp_array = sorted(temp_array, key=lambda x: x[1], reverse= True)
        note_option[key] = temp_array
    return note_option

#we input the generate notes and if the size of generated_notes is one we just find the best possible note, if > 1 then
# we get the bigram frequency.the we calculte the chain of probability by adding one note to the bigram, so it become a trigrams
# then we check how the probability to that the given trigram with the inputted bigram , we store all possible trigram and we randomly (probabilisticlty) c
#choose between the three best option
def find_next_note_in_sequence(generated_notes,option_dict):
    note_tuple = generated_notes[-2:]
    print(note_tuple)
    the_tuple = tuple((note_tuple))
    starting_note = list()
    tuple_count = bigram_dict[tuple((note_tuple))]
    high_prob = 0
    next_note = 0
    note_tuple.append(0)
    for temp_note in range (0,127):
        note_tuple[2] = temp_note
        temp_trigram = note_tuple
        if tuple(temp_trigram) not in trigram_dict:
            continue
        trigram_count = trigram_dict[tuple((temp_trigram))]
        temp_prob = trigram_count/ tuple_count
        starting_note.append(tuple((temp_note,temp_prob)))
        #print('this is the prob', temp_prob, 'of note', temp_note, 'in bigram',the_tuple)
    starting_note.sort(key = lambda x: x[1], reverse= True)
    #print('these are the ', starting_note, ' for bigram', the_tuple)
    if len(starting_note) > 2:
        if random() >= 0.5:
            return starting_note[0][0]
        elif random() < 0.5 and random() > 0.2:
            return  starting_note[1][0]
        else:
            return starting_note[2][0]
    else:
        return starting_note[0][0]
        #here we have toadd a probabilities conditions to break loop repeation for some trigrams

#takes as input on note a generate the note with the highest probability to appear next from the option_dict
def predict_next_note(input_note,option_dict,generated_notes):
    highest_prob = tuple((0,0))
    if input_note in option_dict:
        #note tuple contains (note,probability)
        if len(generated_notes) <  2 :
            highest_prob = option_dict[input_note][0]
        else:
             return find_next_note_in_sequence(generated_notes,option_dict)
    return highest_prob[0]


#given a sequence_length we want to generate a list of notes with size sequence_length by calling predict_next_note
#function sequence_length times by updating the input of the predict_next_note function
def predict_sequence(sequence_length,option_dict):
    ##random generate a note
    random_note = randint(23,100)
    while not bool(option_dict[random_note]):
        random_note = randint(23,100)
    generated_notes = list()
    input_note = random_note
    generated_notes.append(random_note)
    for n in range (sequence_length):
        #print('this is the generate notes', generated_notes)
        generated_notes.append(predict_next_note(input_note,option_dict,generated_notes))
        input_note = generated_notes[len(generated_notes)-1]
    return generated_notes

file_notes = []
bigram_dict = {}
trigram_dict = {}


#make bigram and trigram from midi notes and calculate their frequency
def n_grams_frequency(dt):
    file_notes.append(dt)
    for notes in file_notes:
        for index,el in enumerate(notes):
            if index+1 < len(notes):
                if bool(bigram_dict):
                    if tuple((el,notes[index+1])) not in bigram_dict.keys():
                                bigram_dict[tuple((el,notes[index+1]))]= 1
                    else:
                        bigram_dict[tuple((el,notes[index+1]))] += 1
                else:
                    bigram_dict[tuple((el,notes[index+1]))] = 1
    for notes in file_notes:
        for index,el in enumerate(notes):
            if index+2 < len(notes):
                if tuple((el,notes[index+1],notes[index+2])) not in trigram_dict.keys():
                            trigram_dict[tuple((el,notes[index+1],notes[index+2]))]= 1
                else:
                    trigram_dict[tuple((el,notes[index+1],notes[index+2]))] += 1



def init_markov_model(prob_df):
    option_dict = option_df(prob_df)
    #predict_sequence(200,option_dict)
    create_midi(predict_sequence(200,option_dict))
