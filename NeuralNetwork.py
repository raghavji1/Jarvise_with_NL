import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

#creating neurons of the brain of our project

Stemmer= PorterStemmer()

def tokenize(sentece):
    return nltk.word_tokenize(sentece)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokeinzed_sentence, words):
    sentence_words = [stem(word) for word in tokeinzed_sentence]
    bag = np.zeros(len(words),dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] =1
    return bag