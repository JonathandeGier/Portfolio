uurloon = input('Wat verdien je per uur: ')
werkuren = input('hoeveel uur heb je gewerkt: ')

bedrag = float(uurloon) * float(werkuren)
overzicht = str(uurloon) + ' uur werken levert ' + str(bedrag) + ' Euro op'

print(overzicht)