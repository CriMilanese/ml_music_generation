# ML_project
this repo is meant to contain all files for the project of machine learning, course code X_400154

## plan A

### songs generator

Will need to use deep learning.
All viable options include **Tensorflow**, pretty complicated otherwise.
Online resources and examples aim to produce single-instrument monophonic music, ergo do not expect to replace Emilie Lens very soon.
2 types of music format used are **MIDI** and **abc notation** stored in a one-hot fashion to be used as vectors for the neural net. Datasets are mostly proprietary but there is a very complete one, ready to be scraped at [piano-e-competition](http://www.piano-e-competition.com). 
Use RNN, a special kind of CNN that is able to infer new notes
from previous ones, enhanced through a technique called **LSTM** (Long-Short Term Memory).
There seem to be consistent documentation of previous work, research papers like [this](wx405557858.github.io/assets/papers/music_generation.pdf) or [this](https://arxiv.org/abs/1606.04930) or [this](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwjSnbG3_9XnAhUSGewKHUrKB94QFjAAegQIAxAB&url=http%3A%2F%2Fpeople.idsia.ch%2F~juergen%2Fblues%2FIDSIA-07-02.pdf&usg=AOvVaw2yLf-fkPQMoE84ai6bQmF9) which in turn reference many others. The amount of material is granted by the fact that music generation with machine learning has been done since the begin of the century.

## plan B

### botgammon 

adversarial machine learning to make a bot play backgammon.

