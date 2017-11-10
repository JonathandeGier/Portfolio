list = eval(input('Enter list: '))
range = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

for word in list:
    for char in range:
        if char == word[0]:
            print(word)