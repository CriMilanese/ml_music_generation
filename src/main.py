from os import listdir, chdir, getcwd, mkdir
from parse_midi import parse
from dict_to_df import dict_to_dataframe , calc_probability
from managePickles import *
from markov_chain import init_markov_model
import numpy as np
import pandas as pd

chdir('Data')
sum = lambda s1,s2 : s1 + s2
df = pd.DataFrame()
for dirs in listdir():
    if dirs == 'E major':
        init_markov_model(prob_table)
        break

    chdir(dirs)
    for file in listdir():                                                      # file replaces fl
        # print(file)
        # print(dirs)

        note_freq = parse(file, dirs)                                           # note_freq replaces dt

        #make a temp df
        temp_df = pd.DataFrame()
        temp_df = dict_to_dataframe(note_freq)
        if df.empty:
            df = temp_df.copy()
        else:
            df = df.combine(temp_df,sum)
        #print(df.to_string())
        #np.save('../../pickles/'+dirs+'/'+file[:-4], note_freq)
        del note_freq
    prob_table = calc_probability(df)
    #print(prob_table.to_string())
        #del df
    chdir('../')
