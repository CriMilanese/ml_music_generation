import sys
sys.path.append('../../utils')
from os import listdir, chdir, mkdir

import matplotlib.pyplot as plt
import numpy as np
from mido import MidiFile
from manage_pickles import savePk
from get_notes import get_arr_notes


def convert_notes_to_pitch_names(buf):
    return buf

def collect_notes(d0, d1):
    notes = get_arr_notes(d0)
    savePk(notes, d1+tmp)
    del tmp
    del d0
    return notes

def print_save_distribution(nts, d2):
    buckets = 128
    print(nts)
    plt.hist(nts, buckets)
    plt.show()
    plt.save(d2+sys.argv[1]+'.png')

def main():
    dir0 = '../dataset/'
    dir1 = '../pickles/'
    dir2 = 'graphs/'
    nt = collect_notes(dir0, dir1)
    print_save_distribution(nt, dir2)

if __name__ == '__main__':
    main()
