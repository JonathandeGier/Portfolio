file = open('../Files/example', 'r',)
lines = len(file.readlines())
file.close()

file = open('../Files/example', 'r',)
chars = file.read()
file.close()

file = open('../Files/example', 'r',)
words = len(chars.split())
file.close()

print('Line count: ' + str(lines))
print('Word count: ' + str(words))
print('Character count: ' + str(len(chars)))