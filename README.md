# Music generation with machine learning
This project was meant to be the result of an assignment for the course of Machine Leaning at Vrije Unieversiteit - Amsterdam. It became a joint effort to experiment the power of machine learning for music composition, with satisfying results given its time constraints. It is

It is composed of two parts, one exploiting basic probability theories and a second, more advanced, using modern recurrent neural networks, both with the goal of producing a sequence of notes by prepending an input of the same type.

### File structure:
+ src/ \n
_contains the whole python project source code_
+ pickles/ \n
_includes all python data structures in a handy pickle format_
+ midi/ \n
_all MIDI sample files to be parsed are stored here_
+ tex_report/ \n
_all you need to have is the L<sub>A</sub>T<sub>E</sub>X package installed to be able to compile .tex into PDF, but a simple text editor will be enough to edit it_

for more information take a look at the resulting article in the **docs** folder, which is compiled using latex environment

### API

**parse_midi.py**
>`parse(_filename_)`
  performs midi file parsing given a filename and *returns* a dictionary with all notes played in a track as keys, their  following notes and occurrence as values, stored into an array.

**managePickles.py**
  >`loadPk(_filename_)`
  pass a pickle filename to the functions in order to have the data structure returned.
  >`savePk(_data_, _filename_)`
  pass the data structure and a name to save the file with.

**notes_freq.py**
  >An example of how to use *managePickles.py* to retrieve one of the data structures, the printed result contains a dictionary with note to frequency key-value pairs.

**main.py**
  >performs parsing for all .MID files from the "midi/" folder and save their content as pickle files into "pickles/".

**__init__.py**
  >allows users to export this directory into PYTHONPATH env variable for usage of the methods outside this folder
