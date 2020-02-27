from os import listdir, chdir, getcwd, mkdir
from parse_midi import parse
from managePickles import *
import numpy as np

chdir('midi')
for dirs in listdir():
    mkdir('../pickles/'+dirs)
    chdir(dirs)
    for fl in listdir():
        print(fl)
        dt = parse(fl)
        np.save('../../pickles/'+dirs+'/'+fl[:-4], dt)
        del dt
    chdir('../')
