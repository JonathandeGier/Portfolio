def print_menu():
    'print het menu en vraagt om keuze van de klant'
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: ik wil een nieuwe kluis')
    print('3: ik wil even iets uit mijn kluis halen')
    print('4: ik geef mijn kluis terug')
    print('5: ik wil stoppen')
    print()

    klantmenukeuze = int(input('Uw keuze: '))
    return klantmenukeuze

def leesfile(textfile):
    'leest de file en geeft een lijst met elke regel terug'
    kluizen = open(textfile)
    inkluizenfile = kluizen.readlines()                                                                                 # opent de file en plaatst elke regel als string in een list
    kluizen.close()
    return inkluizenfile

def toon_aantal_kluizen_vrij():
    'heeft string met de naam van de file nodig en geeft een integer met het aantal beschikbare kluizen terug'
    aantal_vrije_kluizen = aantalkluizen - len(lijstmetdekluizen)                                                       # berekend hoeveel kluizen er nog beschikbaar zijn

    if aantal_vrije_kluizen > 1:                                                                                        # \
        print('Er zijn {} kluizen beschikbaar'.format(aantal_vrije_kluizen))                                            #  \
    elif aantal_vrije_kluizen == 1:                                                                                     #   \
        print('Er is nog maar {} kluis beschikbaar'.format(aantal_vrije_kluizen))                                       # zorgt ervoor dat er een gramaticaal correcte zin uit komt
    else:                                                                                                               #   /
        print('Er zijn geen kluizen meer beschikbaar')                                                                  #  /

def nieuwe_kluis(userpassword):
    'heeft string met de naam van de file nodig met een wachtwoord en maakt een nieuwe kluis in de file'
    global kluizenlijst
    inkluizenfile = lijstmetdekluizen

    onbeschikbarekluislijst = kluislijstnummer
    for kluis in inkluizenfile:                                                                                                 # maakt lijst met alle onbeschikbare kluizen
        kluisnummer = kluis.split(';')
        onbeschikbarekluislijst = onbeschikbarekluislijst + [kluisnummer[0]]

    lijstmetbeschikbarekluizen = list(kluizenlijst)                                                                             # maakt lijst met alle beschikbare kluizen

    for kluis in onbeschikbarekluislijst:
        lijstmetbeschikbarekluizenindex = lijstmetbeschikbarekluizen.index(kluis)                                               # kijkt op welke plek de onbeschikbare kluis staat in de lijst met beschikbare kluizen
        lijstmetbeschikbarekluizen.remove(lijstmetbeschikbarekluizen[lijstmetbeschikbarekluizenindex])                          # verwijderd de onbeschikbare kluis van de lijst met beschikbare kluizen

    kluisnummer = lijstmetbeschikbarekluizen[0]                                                                                 # geeft klant eerste beschikbare kluis

    lijstmetdekluizen.append('{};{}\n'.format(kluisnummer, userpassword))

    return kluisnummer                                                                                                          # geeft kluisnummer terug om tegen de klant te kunnen zeggen welk kluisnummer hij/zij heeft

def toon_nieuwe_kluis():
    if aantalkluizen - len(lijstmetdekluizen) != 0:                                                                             # kijkt of er nog kluizen beschikbaar zijn
        code = input('Voer een code voor uw kluis in: ')                                                                        # vraagt om wachtwoord
        if len(code) > minimalelengtewachtwoord - 1:                                                                            # kijkt of wachtwoord lang genoeg is
            print('U heeft nu kluisnummer {} met de code die u zojuist heeft ingevoerd'.format(nieuwe_kluis(code)))             # wachtwoord is lang genoeg
        else:
            print(
                'Uw code is niet lang genoeg.\nMoet minimaal 4 karakters lang zijn.\nBegin opnieuw')                            # wachtwoord is niet lang genoeg
    else:
        print('Er zijn geen kluizen meer beschikbaar')

def kluis_openen(kluisnummer, userpassword):
    'kijkt of combinatie kluisnummer en userparrword overeenkomen in de fle textfile en geeft True terug als het correct is'
    uitkomst = False
    for kluis in lijstmetdekluizen:
        kluissep = kluis.split(';')
        if kluissep[0] == kluisnummer and kluissep[1] == userpassword:                                                          # kijkt of kluisnummer met wachtwoord overeenkomen
            uitkomst = True                                                                                                         # als er een goede combinatie gevonden is stopt de functie en geeft True terug
            break
    return uitkomst

def toon_kluis_open():
    kluisnummer = input('Voer het nummer van uw kluis in: ')  # vraagt om kluisnummer en wachtwoord
    code = input('voer het wachtwoord van uw kluis in: ') + '\n'

    iscombinatiecorrect = kluis_openen(kluisnummer, code)  # kijkt of combinatie correct is

    if iscombinatiecorrect:
        print('U heeft de goede combinaties ingevult, uw kluis is open!')  # als combinatie goed is
    else:
        print('Kluisnummer of wachtwoord klopt niet, probeer opnieuw')

def kluis_teruggeven_deel1(kluisnummer, userpassword):
    'feitelijk hetzelfde als de functie kluis_openen(), maar geeft het kluisnummer terug'

    uitkomst = False
    for kluis in lijstmetdekluizen:
        kluissep = kluis.split(';')
        if kluissep[0] == kluisnummer and kluissep[1] == userpassword:                                                          # kijkt of kluisnummer met wachtwoord overeenkomen
            uitkomst = kluis
            break                                                                                                               # als er een goede combinatie gevonden is stopt de functie en geeft de betrefte regel terug
    return uitkomst

def kluis_teruggeven(kluis):
    'verwijderd kluis uit textfile'
    lijstmetdekluizen.remove(kluis)                                                                                                 # verwijderd regel uit de list

def toon_kluis_teruggeven():
    kluisnummer = input('Voer het nummer van uw kluis in: ')
    code = input('voer het wachtwoord van uw kluis in: ') + '\n'

    iscombinatiecorrect = kluis_openen(kluisnummer, code)  # hetzelfde als klant de kluis wilt openen

    if iscombinatiecorrect:
        kluis_teruggeven(kluis_teruggeven_deel1(kluisnummer, code))  # verwijderd kluis uit de file als combinatie correct is
        print('De kluis is nu weer beschikbaar')
    else:
        print('Kluisnummer of wachtwoord klopt niet, probeer opnieuw')

def schrijf_kluizen_weg(textfile, lijstmetdekluizen):

    kluizen = open(textfile, 'w')                                                                                       # opent de file en zorgt ervoor dat we kunnen schrijven
    for kluis in lijstmetdekluizen:
        kluizen.write(kluis)                                                                                            # schrijft alle kluizen weer op, maar nu zonder regel
    kluizen.close()

# variablen die in functies worden gebruikt
kluizenlijst = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
aantalkluizen = len(kluizenlijst)
kluislijstnummer = []
minimalelengtewachtwoord = 4
kluizenfile = 'Files/kluizen'

klantwiltdoorgaan = True
lijstmetdekluizen = leesfile(kluizenfile)

# while loop zodat code niet steeds opnieuw op hoeft te starten
while klantwiltdoorgaan:

    klantmenukeuze = print_menu()

    if klantmenukeuze == 1:                                                                                                     # als klant wilt weten hoeveel kluizen er nog vrij zijn

        toon_aantal_kluizen_vrij()

    elif klantmenukeuze == 2:                                                                                                   # als klant een kluis wilt hebben

        toon_nieuwe_kluis()

    elif klantmenukeuze == 3:                                                                                                   # als klant iets uit zijn/haar kluis wilt halen

        toon_kluis_open()

    elif klantmenukeuze == 4:                                                                                                   # als klant de kluis terug wilt geven

        toon_kluis_teruggeven()

    elif klantmenukeuze == 5:                                                                                                   # als de klant weg gaat

        klantwiltdoorgaan = False
        schrijf_kluizen_weg(kluizenfile, lijstmetdekluizen)

    else:
        print('Ongeldige waarde')                                                                                               # als klant een optie kiest die niet kan

print('Bedankt en tot ziens!')                                                                                                  # afscheid nemen van klant
