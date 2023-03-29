import pytest
import re

# Writing text file into a string
filename = "text.txt"
with open(filename, 'r') as file:
    sentence = file.read()

# Getting number of sentences
def numberOfSentences(sentence):
    sentences = re.findall(r'[\w\s]*[\.\?!]+|[\w\s]*\.{3}', sentence)
    numSentences = len(sentences)
    return numSentences

# Getting number of words
def numberOfWords(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    numWords = len(words)
    return numWords


def testNumberOfSentences():
    assert numberOfSentences(sentence) == 1

def testNumberOfWords():
    assert numberOfWords(sentence) == 18