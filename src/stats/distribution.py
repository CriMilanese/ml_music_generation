import sys
sys.path.append('../../utils')
from os import listdir, chdir, mkdir

import matplotlib.pyplot as plt
import numpy as np
from mido import MidiFile
from manage_pickles import savePk
from get_notes import get_arr_notes

dir0 = '../dataset/'
dir1 = '../pickles/'
dir2 = 'graphs/'

def collect_notes():
    notes = get_arr_notes(dir0)
    savePk(notes, dir1+tmp)
    del tmp
    del dir0
    return notes

def print_save_distribution(nts):
    buckets = 128
    plt.hist(nts, buckets)
    plt.show()
    plt.save(dir2+sys.argv[1]+'.png')

def main():
    nt = collect_notes()
    print_save_distribution(nt)

if __name__ == '__main__':
    main()
