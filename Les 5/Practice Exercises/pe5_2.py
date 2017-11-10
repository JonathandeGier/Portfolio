# deel 1 van de opdracht
kaarten = open('../Files/kaartnummers', 'w')

kaarten.write('325255, Jan Jansen \n')
kaarten.write('334343, Erik Materus \n')
kaarten.write('235434, Ali Ahson \n')
kaarten.write('645345, Eva Versteeg \n')
kaarten.write('534545, Jan de Wilde \n')
kaarten.write('345355, Henk de Vries \n')

kaarten.close()

# deel 2 van de opdracht
kaarten = open('../Files/kaartnummers', 'r')
inkaarten = kaarten.readlines()
kaarten.close()

for kaart in inkaarten:
    info = kaart.split(',')
    info[1] = info[1].replace('\n', '')
    print('{} heeft kaartnummer: {}'.format(info[1], info[0]))