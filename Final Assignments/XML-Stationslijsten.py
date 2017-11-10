def toon_code_type():
    print('Dit zijn de codes en types van de {} stations: '.format(len(stationsDictLijst)))
    for station in stationsDictLijst:
        if station is not None:
            print('{:4} - {}'.format(station.get('Code'), station.get('Type')))

def toon_synoniemen():
    synoniemstationslijst = []

    for station in stationsDictLijst:
        if station is not None:
            if station.get('Synoniemen') is not None:
                synoniemstationslijst += [station]

    print()
    print('Dit zijn alle stations met één of meer synoniemen:')
    if len(synoniemstationslijst) > 0:
        for station in synoniemstationslijst:
            if station is not None:
                print('{:4} - {}'.format(station.get('Code'), station.get('Synoniemen')))
    else:
        print('Er zijn geen stations met synoniemen')

def toon_volledige_naam():
    print()
    print('Dit is de lange naam van elk station:')
    for station in stationsDictLijst:
        if station is not None:
            print('{:4} - {}'.format(station.get('Code'), station.get('Namen').get('Lang')))


import xmltodict
file = 'Files/XMLStations'

with open(file, 'r') as lezen:
    inhoudstations = lezen.read()

stationsDict = xmltodict.parse(inhoudstations)

if stationsDict.get('Stations') is not None:
    stationsDictLijst = stationsDict.get('Stations').get('Station')

    toon_code_type()
    toon_synoniemen()
    toon_volledige_naam()
