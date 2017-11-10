zin = input('Typ een willeleurige zin: ')

def gemiddelde(zin_met_woorden):
    woorden = zin_met_woorden.split()
    woordlengte = int()
    for woord in woorden:
        woordlengte = woordlengte + len(woord)
    gem = woordlengte / len(woorden)
    return gem

print('Gemiddelde lengte van een woord in deze zin is ' + str(round(gemiddelde(zin), 1)) + ' karakters')