from os import listdir, chdir, getcwd, mkdir
from parse_midi import parse,n_grams_frequency
from dict_to_df import dict_to_dataframe , calc_probability
from markov_chain import init_markov_model
import numpy as np
import pandas as pd

sum = lambda s1,s2 : s1+ s2
df = pd.DataFrame()
dirs_counter = 0
for dirs in listdir('Data'):
    for fl in listdir('Data/'+ dirs):
        print('Data/'+dirs+'/'+fl)
        print('Data/'+dirs)
        ##first get dirs
        note_freq = parse('Data/'+dirs+'/'+fl,'Data/'+dirs)
        temp_df = pd.DataFrame()
        temp_df = dict_to_dataframe(note_freq)
        if df.empty:
            df = temp_df.copy()
        else:
            df = df.combine(temp_df,sum)
        del note_freq
    prob_table = calc_probability(df)
init_markov_model(prob_table)
