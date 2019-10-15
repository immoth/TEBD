# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:41:29 2019

@author: jsten
"""

import pickle

def save(file,tensor):
    with open(file,"wb") as f:
        pickle.dump(tensor,f)

def load(file):
    with open(file,"rb") as f:
        ltp=pickle.load(f)
    return ltp