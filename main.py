from os import listdir, chdir, getcwd, mkdir
from parse_midi import parse
from dict_to_df import dict_to_dataframe , calc_probability
from managePickles import *
import numpy as np
import pandas as pd

chdir('midi')
sum = lambda s1,s2 : s1+ s2
df = pd.DataFrame()
for dirs in listdir():
    #mkdir('../pickles/'+dirs)
    chdir(dirs)
    for fl in listdir():
        print(fl)
        print(dirs)
        dt = parse(fl)
        #make a temp df
        temp_df = pd.DataFrame()
        temp_df = dict_to_dataframe(dt)
        if df.empty:
            df = temp_df.copy()
        else:
            df = df.combine(temp_df,sum)
        #print(df.to_string())
        #np.save('../../pickles/'+dirs+'/'+fl[:-4], dt)
        del dt
    prob_table = calc_probability(df)
    print(prob_table.to_string())
        #del df
    chdir('../')
