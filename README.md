# Music generation with machine learning
This project was meant to be the result of an assignment for the course of Machine Leaning at Vrije Unieversiteit - Amsterdam. It became a joint effort to experiment the power of machine learning for music composition, with satisfying results given its time constraints. It is

It is composed of two parts, one exploiting basic probability theories and a second, more advanced, using modern recurrent neural networks, both with the goal of producing a sequence of notes by prepending an input of the same type

## Hidden Markov Model

## Long Short Term Memory



<!-- ### songs generator

Will need to use deep learning. All viable options include **Tensorflow**, pretty complicated otherwise.
Online resources and examples aim to produce single-instrument monophonic music. Two types of music format are used, namely **MIDI** and **abc notation** stored in a one-hot fashion to be used as vectors for the neural net. Datasets are mostly proprietary but there is a very complete one, ready to be scraped at [piano-e-competition](http://www.piano-e-competition.com).
Use **RNN**, a special kind of CNN that is able to infer new notes
from previous ones, enhanced through a technique called **LSTM** (Long-Short Term Memory).
There seem to be consistent documentation of previous work, research papers like [this](wx405557858.github.io/assets/papers/music_generation.pdf) or [this](https://arxiv.org/abs/1606.04930) or [this](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjSnbG3_9XnAhUSGewKHUrKB94QFjAAegQIAxAB&url=http%3A%2F%2Fpeople.idsia.ch%2F~juergen%2Fblues%2FIDSIA-07-02.pdf&usg=AOvVaw2yLf-fkPQMoE84ai6bQmF9) which in turn reference many others. The amount of material is granted by the fact that music generation with machine learning has been done since the begin of the century.

#### parser
+ src/
  _contains the whole python project source code_
  + pickles/
  _includes all python data structures in a handy pickle format_
  + midi/
  _all MIDI sample files to be parsed are stored here_
+ \_\_pycache__
  _contains the compiled bytecode of our files_
+ tex_report/
  _all you need to have is the L<sub>A</sub>T<sub>E</sub>X package installed to be able to compile .tex into PDF, but a simple text editor will be enough to edit it_

### API
In order to import any of the below methods from the same folder
  `from file import method`
In order to import methods from files that are stored in different folders, this folder path must be added to PYTHONPATH environmental variable.
  `export PYTHONPATH="${PYTHONPATH}:/this/very/path"`
Or for Windows users, check out the list of environmental variables under "system settings".
All methods listed here handle the source/destination directory by themselves. Make sure to run them from "src/". -->

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
