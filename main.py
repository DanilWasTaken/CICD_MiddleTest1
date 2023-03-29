f = open("text.txt", "r")
sentence = ''

for x in f:
  sentence += x

f.close()

print(sentence)