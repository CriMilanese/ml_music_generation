# this file is meant to retrieve data from a pickle file
# pickle files are serialized version of python data structure

###############################################################
# to make use of this tool simply use the import in your script
# from managePickles import loadPk
###############################################################

import pickle

# load from caller local directory
def loadPk(filename):
    my_list = ''
    with open('{}.pickle'.format(filename), 'rb') as handle:
        my_list = pickle.load(handle)
    handle.close()
    return my_list

#saves in caller local directory
def savePk(data, filename):
    with open('{}.pickle'.format(filename), 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    del data
    handle.close()

def printPk(data, filename):
    pk = loadPk(filename)
    print(pk)
