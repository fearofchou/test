# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 21:03:54 2014

@author: fearofchou
"""
import cPickle as pickle

def save(filename,data):
    with open(filename, 'wb') as outfile:
        pickle.dump(data, outfile, pickle.HIGHEST_PROTOCOL)

def load(filename):
    with open(filename, 'rb') as infile:
        x = pickle.load(infile)
    return x