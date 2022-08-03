from textgenrnn import textgenrnn

textgen = textgenrnn("textgenrnn_weights.hdf5")
textgen.train_from_file("message.txt")
textgen.save("model")
