#! /usr/bin/env python3

import spacy, en_core_web_sm
import numpy as np
from numpy import dot
from numpy.linalg import norm
import matplotlib.pyplot as plt
from math import sqrt

import umap

nlp = spacy.load('en_core_web_sm')
nlp = en_core_web_sm.load()
doc = nlp(open("encyclopedia.txt").read())

tokens = list(set([w.text for w in doc if w.is_alpha]))

def vec(s):
    return nlp(s).vector

def length(v1, v2):
    return sqrt(dot(v2 - v1, v2 - v1))

def spacy_closest(token_list, vec_to_check, n=10):
    return sorted(token_list,
                  key=lambda x: length(vec_to_check, vec(x)))[:n]

word_vecs = [
    vec(w) for w in tokens
]

reducer = umap.UMAP()
embedding = reducer.fit_transform(word_vecs)

fig, ax = plt.subplots()

def onclick(event):
    inv_transformed_points = reducer.inverse_transform([[event.xdata, event.ydata]])
    closest_vec = spacy_closest(tokens, inv_transformed_points[0], 1)
    print((event.xdata, event.ydata))
    print(closest_vec)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

ax.scatter(
    embedding[:, 0],
    embedding[:, 1],
    s=0.15
)
plt.show()