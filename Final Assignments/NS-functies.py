def standaardprijs(afstandKM):
    'berekend de standaardprijs zonder korting en geeft die terug'
    if afstandKM >= langeafstandsgrens:
        prijs = basislangeafstandsprijs + (afstandKM * langeafstandsprijsKM)            # berekend de prijs als de rit langer is dan langeafstandsgerens km
    else:
        prijs = korteafstandsprijsKM * afstandKM                                        # berekend de prijs als de rit kleiner is dan langeafstandsgrens km
    return prijs

def ritprijs(weekendrit, afstandKM):
    'berekend de prijs met de korting en geeft de definitieve prijs terug'
    normaalprijs = standaardprijs(afstandKM)                                            # bereken prijs zonder korting
    if weekendrit:
        if heeftrechtopleeftijdkorting:
            prijs = normaalprijs * weekendenleeftijdkorting                             # bereken prijs voor weekend met leeftijd <= 12 of >= 65
        else:
            prijs = normaalprijs * weekendkorting                                       # bereken prijs voor weekend met leeftijd tussen 12 en 65
    else:
        if heeftrechtopleeftijdkorting:
            prijs = normaalprijs * leeftijdkortinggeenweekend                           # bereken prijs voor werkdagen met leeftijd <=12 of >= 65
        else:
            prijs = normaalprijs                                                        # bereken prijs voor werkdagen met leeftijd tussen 12 en 65
    return prijs

# inputvariablen
afstand = int(input('Ritafstand in km: '))
weekend = False
leeftijd = int(input('Leeftijd: '))

# variablen voor functie standaardprijs()
langeafstandsgrens = 50
langeafstandsprijsKM = 0.6
korteafstandsprijsKM = 0.8
basislangeafstandsprijs = 15

# variablen voor functie ritprijs()
minleeftijdkorting = 12
maxleeftijdkorting = 65
heeftrechtopleeftijdkorting = leeftijd <= minleeftijdkorting or leeftijd >= maxleeftijdkorting
weekendenleeftijdkorting = 0.65
weekendkorting = 0.60
leeftijdkortinggeenweekend = 0.70

if afstand < 0:                                                                         # maakt de afstand 0 als het negatief is
    afstand = 0

defprijs = str(round(ritprijs(weekend, afstand), 2))                                    # berekend de definitieve prijs met ritprijs(),
                                                                                        # rond het af op 2 decimalen en maakt er een string van

print('De prijs voor deze rit is: € {}'.format(defprijs))                               # print de prijs
