#!/usr/bin/python3i

def multiple_returns(sentence):
    lens = len(sentence)
    if sentence is None:
        return(None, sentence[0])
    else:
        return(lens, sentence[0])
