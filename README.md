# Music generation with machine learning
This project was meant to be the result of an assignment for the course of Machine Leaning at Vrije Unieversiteit - Amsterdam. It became a joint effort to experiment the power of machine learning for music composition, with satisfying results given its time constraints. It is

It is composed of two parts, one exploiting basic probability theories and a second, more advanced, using modern recurrent neural networks, both with the goal of producing a sequence of notes by prepending an input of the same type.

### File structure:
+ `src/`
    _contains the whole python project source code_
  + `dataset`
    _includes a zip file with the midi files generated after key normalization_
  + `HMM`
    _contains the main functions for the generation of songs with the Hidden Markov Model_
  + `LSTM`
  _contains the main functions for the generation of songs with the Recurrent Neural Network_
  + `midi/`
  _all MIDI sample files to be parsed are stored here_
  + `pickles/`
    _includes all python data structures in a handy pickle format_
  + `stats/`
    _contains a script to perform basic statistical analysis on the midi files produced after normalization_
+ `docs/`
  _the full article describing the experiment in-depth and the tex file, where the article came from, is there as an example to look at._
+ `utils`
_helpers for most of the operations done through the experiment, they might find application elsewhere, take a look at the API section._

for more information take a look at the resulting article in the **docs** folder, which is compiled using latex environment.

We got the models to produce [two songs](https://soundcloud.com/user-748655368), which were then the subject of a [survey]() to find out which of the result people liked the most.
