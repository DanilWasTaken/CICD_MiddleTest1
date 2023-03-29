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
    num_sentences = len(sentences)
    return num_sentences

print(f'Number of sentences is: {numberOfSentences(sentence)}')