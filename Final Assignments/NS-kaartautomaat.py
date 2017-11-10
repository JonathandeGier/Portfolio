def print_traject(stations):
    print('Traject van deze trein:')
    for station in range(len(stations)):
        if station != len(stations) - 1:
            print(stations[station], end=' --> ')
        else:
            print(stations[station])
    print()

def inlezen_beginstation(stations):

    while True:
        beginstation = input('Wat is je beginstation? : ')
        if beginstation == stations[-1]:
            print('{} is de einbestemming van deze trein, kies een ander station'.format(beginstation))
        elif beginstation in stations:
            break
        else:
            print('Deze trein komt niet in {}'.format(beginstation))

    return beginstation

def inlezen_eindstation(stations, beginstation):

    while True:
        eindstation = input('Wat is je eindstation? : ')
        if eindstation in stations:

            if stations.index(eindstation) > stations.index(beginstation):
                break
            elif stations.index(eindstation) == stations.index(beginstation):
                print('U bent al in {}, het heeft gaan zin om hiervoor een treinkaartje te kopen'.format(eindstation))
            else:
                print('Deze trein gaat niet richting {}'.format(eindstation))

        else:
            print('Deze trein komt niet in {}'.format(eindstation))

    return eindstation

def omroepen_reis(stations, beginstation, eindstation):

    print()
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, stations.index(beginstation) + 1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, stations.index(eindstation) + 1))

    afstand = stations.index(eindstation) - stations.index(beginstation)
    print('de afstand bedraagd {} station(s)'.format(afstand))
    print('de prijs van het kaartjeis {} euro'.format(afstand * 5))
    print()
    print('Jij stapt in de trein in: {}'.format(beginstation))

    for station in stations[stations.index(beginstation) + 1:stations.index(eindstation)]:
        print('  -  {}'.format(station))

    print('Jij stapt uit in: ' + eindstation)


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
# stations2 = ['Rhenen', 'Veenendaal Centrum', 'Veenendaal West', 'Maarn', 'Driebergen-Zeist', 'Bunnik', 'Utrecht Vaartsche Rijn', 'Utrecht Centraal']
print_traject(stations)
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
