# this file contains 

from parse_midi import parse
import pandas as pd
import numpy as np
from sys import argv

def dict_to_dataframe(input_dict):
    df = pd.DataFrame(np.zeros((128,128)), dtype= int)
    temp_df = pd.DataFrame(input_dict)
    for key in input_dict.keys():
        df.loc[key, : ] = temp_df.loc[:,key]
    return df

def calc_probability(freq_df):
    prob_df = pd.DataFrame(np.zeros((128,128)), dtype= float)
    for index, row in freq_df.iterrows():
        row_sum = row.sum()
        if row_sum < 1 :
            continue
        print('this is the sum', row_sum)
        for index1, col in freq_df.iteritems():
            proba = (freq_df[index1][index]) / (row_sum)
            prob_df[index1][index] = float(proba)
    return prob_df
