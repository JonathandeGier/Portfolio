invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
gesorteerdelijst = []

gesorteerdelijststring = invoer.split('-')
gesorteerdelijststring.sort()

for string in gesorteerdelijststring:
    getal = int(string)
    gesorteerdelijst = gesorteerdelijst + [getal]

grootstegetal = max(gesorteerdelijst)
kleinstegetal = min(gesorteerdelijst)

aantalgetallen = len(gesorteerdelijst)
somgetallen = sum(gesorteerdelijst)

gemiddelde = somgetallen / aantalgetallen

print('Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} en Som van de getallen: {}\nGemiddelde: {}'.format(gesorteerdelijst, grootstegetal, kleinstegetal, aantalgetallen, somgetallen, gemiddelde))

