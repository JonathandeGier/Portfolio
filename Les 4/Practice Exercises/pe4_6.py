lijst = eval(input('Lijst met letters: '))

def wijzig(letterlijst):
    letterlijst[0] = 'd'
    letterlijst[1] = 'e'
    letterlijst[2] = 'f'

wijzig(lijst)
print(lijst)
