import csv

bestand = '../Files/Artiekelen'

with open(bestand, 'r') as CSVArtiekelen:
    artiekelen = csv.DictReader(CSVArtiekelen, delimiter=';')

    voorraadsom = 0
    duursteartiekel = {'Prijs':0.00}
    minstinvoorraadartiekel = {'Voorraad':10000000000000000000000}
    for artiekel in artiekelen:
        if float(artiekel.get('Prijs')) > float(duursteartiekel.get('Prijs')):
            duursteartiekel = artiekel

        if int(artiekel.get('Voorraad')) < int(minstinvoorraadartiekel.get('Voorraad')):
            minstinvoorraadartiekel = artiekel

        voorraadsom += int(artiekel.get('Voorraad'))

    print('Het duurste artiekel is {} en die kost {} Euro'.format(duursteartiekel.get('Naam'), duursteartiekel.get('Prijs')))
    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(minstinvoorraadartiekel.get('Voorraad'), minstinvoorraadartiekel.get('Artikelnummer')))
    print('In totaal hebben wij {} producten in ons magazijn liggen'.format(voorraadsom))
