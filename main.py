import re

# Writing text file into a string
filename = "text.txt"
with open(filename, 'r') as file:
    sentence = file.read()

# String output
print(sentence)

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

print(f'Number of sentences is: {numberOfSentences(sentence)}')
print(f'Number of sentences is: {numberOfWords(sentence)}')