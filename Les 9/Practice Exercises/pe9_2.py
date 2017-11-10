import datetime
import csv

bestand = '../Files/inloggers.csv'

while True:
    naam = input("Wat is je achternaam? ")
    if naam == '':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    with open(bestand, 'r') as CSVFile:
        inloggers = csv.reader(CSVFile, delimiter=';')

        persoonNietInInloggers = True
        for persoon in inloggers:
            if persoon[1] == naam and persoon[2] == voorl and persoon[3] == gbdatum and persoon[4] == email:
                persoonNietInInloggers = False
                print()

    if persoonNietInInloggers:
        today = datetime.datetime.today()
        logintime = today.strftime('%a %d %b %Y at %H:%M')

        with open(bestand, 'a', newline='') as CSVFile:
            writer = csv.writer(CSVFile, delimiter=';')
            writer.writerow((logintime, naam, voorl, gbdatum, email))
            print()