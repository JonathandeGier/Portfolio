doorgaan = True

while doorgaan:
    woord = input('Geef een string van vier letters: ')

    if len(woord) == 4:
        print()
        break
    else:
        print('{} heeft {} letters'.format(woord, len(woord)))

print('Inlezen van correcte string: {} is geslaagd'.format(woord))
