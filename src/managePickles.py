# this file is meant to retrieve data from a pickle file
# pickle files are serialized version of python data structure

###############################################################
# to make use of this tool simply use the import in your script
# make sure to be in the 'src' directory
# from loadPickle import loadPk
###############################################################

import pickle

def loadPk(filename):
    with open('pickles/' + filename, 'rb') as handle:
        my_list = pickle.load(handle)
        return my_list

def savePk(data, filename):
    with open('pickles/'+filename+'.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
