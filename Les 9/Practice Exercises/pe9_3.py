import csv
bestand = '../Files/gamers'

with open(bestand, 'r') as CSVGamers:
    gamers = csv.reader(CSVGamers, delimiter=';')

    infolist = []
    scores = []
    for gamer in gamers:
        infolist += [gamer]
        scores += [int(gamer[2])]

    topscore = max(scores)
    topscoreindex = scores.index(topscore)
    topscoreinfo = infolist[topscoreindex]

    print('De hoogste score is: {} op {} behaald door {}'.format(topscoreinfo[2], topscoreinfo[1], topscoreinfo[0]))
