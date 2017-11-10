bruin = {'Best', 'Beukenlaan', "Helmond 't Hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Best', 'Beukenlaan', 'Geldrop', 'Heeze', 'Weert'}

print(bruin.intersection(groen))

print('alleen bruin: {}'.format(bruin.difference(groen)))

print('alle stations op bruin: {}'.format(bruin))
print('alle stations op groen: {}'.format(groen))