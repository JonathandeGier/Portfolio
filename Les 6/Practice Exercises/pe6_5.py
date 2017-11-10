maxindex = 10
maxtafel = 10

for tafel in range(1, maxtafel + 1):
    print('Tafel van {}'.format(tafel))
    for index in range(1, maxindex + 1):
        antwoord = index * tafel
        print('{} x {} = {}'.format(index, tafel, antwoord))
    print()