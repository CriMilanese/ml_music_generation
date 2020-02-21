# this module shows an implementation for importing
# pickle files into a variable

import re
import numpy
from loadPickle import loadPk

my_list = loadPk("note2freq.pickle")

print(my_list)
