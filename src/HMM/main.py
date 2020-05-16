import sys
sys.path.append('../../utils')
from os import listdir, chdir, getcwd, mkdir
from parse_midi import parse
from dict_to_df import dict_to_dataframe , calc_probability
from managePickles import *
from markov_chain import init_markov_model
# import numpy as np
import pandas as pd

def main(scale):
    chdir('../dataset')
    sum = lambda s1,s2 : s1 + s2
    sca = scale + " major"
    df = pd.DataFrame()
    for dirs in listdir():
        prob_table = calc_probability(df)
        if dirs == sca:
            chdir(dirs)
            for file in listdir():
            note_freq = parse(file, dirs)
            temp_df = pd.DataFrame()
            temp_df = dict_to_dataframe(note_freq)
            if df.empty:
                df = temp_df.copy()
            else:
                df = df.combine(temp_df,sum)
                del note_freq
            init_markov_model(prob_table)
            break
        else:
            print("scale not available")
            return
        chdir('../')

if __name__ == '__main__':
    scale = raw_input("please insert the key of the song: [C, E, G] \n> ")
    main(scale)
