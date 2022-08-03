#!/bin/python
from textgenrnn import textgenrnn

textgen = textgenrnn("textgenrnn_weights.hdf5")
textgen.train_from_file("message.txt", num_epochs=1)
textgen.save("model.hdf5")
