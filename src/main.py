import os
from parse_midi import parse
from managePickles import *

os.chdir(os.getcwd()+'/midi/')
for indx, file in enumerate(os.listdir(os.getcwd())):
    if file.endswith('.MID'):
        my_dict = parse(file)
        os.chdir('../')
        savePk(my_dict, file[:-4])
