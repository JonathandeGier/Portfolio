woord = input('Woord: ')

def ion2e(woordion):
    if woordion[-3] == 'i' and woordion[-2] == 'o' and woordion[-1] == 'n':
        woordion[-3] = 'e'
        woordion[-1] = ''
        woordion[-1] = ''
    return woordion

print(ion2e(woord))