def seizoen(maand):
    if maand > 11:
        seizoen = 'winter'
    elif maand > 8:
        seizoen = 'herfst'
    elif maand > 5:
        seizoen = 'zomer'
    elif maand > 2:
        zeizoen = 'lente'
    else:
        seizoen = 'winter'
    return seizoen

welkemaand = int(input('geef een maand in integer: '))

if welkemaand < 13:
    print('Maand {} is in de {}.'.format(welkemaand, seizoen(welkemaand)))
else:
    print('Maand {} bestaat niet!'.format(welkemaand))