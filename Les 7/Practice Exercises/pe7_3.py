progcijfers = {'Rik':7.3, 'Bas': 6.4, 'Ruben': 9.3, 'Silv':9.8, 'Jonathan':10, 'Luuk':8.4, 'Lianne':9.2, 'Ron':4.8}

for item in progcijfers.items():
    if item[1] >= 9.0:
        print('{} heeft een {}'.format(item[0], item[1]))
