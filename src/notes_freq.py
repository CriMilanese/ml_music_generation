# this module shows an implementation for importing
# pickle files into a variable

from managePickles import loadPk
from sys import argv

my_list = loadPk(argv[1])

print(my_list)
