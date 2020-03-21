# this file is meant to retrieve data from a pickle file
# pickle files are serialized version of python data structure

###############################################################
# to make use of this tool simply use the import in your script
# make sure to be in the 'src' directory
# from managePickles import loadPk
###############################################################

import pickle

def loadPk(filename):
    my_list = ''
    with open('{}.pickle'.format(filename), 'rb') as handle:
        my_list = pickle.load(handle)
    handle.close()
    return my_list

def savePk(data, filename):
    with open('{}.pickle'.format(filename), 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    del data
    handle.close()

def printPk(data, filename):
    pk = loadPk(filename)
    print(pk)
