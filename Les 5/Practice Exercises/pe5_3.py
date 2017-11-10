kaarten = open('../Files/kaartnummers', 'r')
inkaarten = kaarten.readlines()
kaarten.close()
nummers = []

for kaart in inkaarten:
    info = kaart.split(',')
    nummers = nummers + [info[0]]

aantalregels = len(nummers)
nummer = max(nummers)
regel = nummers.index(nummer) + 1
print('Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}'.format(aantalregels, nummer, regel))
