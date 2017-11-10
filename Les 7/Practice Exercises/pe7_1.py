lijstmetgetallen = []
doorgaan = True

while doorgaan:
    getal = int(input('Geef een getal: '))

    if getal != 0:
        lijstmetgetallen.append(getal)
    else:
        doorgaan = False

aantalgetallen = len(lijstmetgetallen)
somgetallen = sum(lijstmetgetallen)

print('Er zijn {} getallen ingevoerd, de som is: {}'.format(aantalgetallen, somgetallen))
