lijst = eval(input('Lijst met getallen: '))

def kwadraten_som(grondgetallen):
    resultaat = 0
    for getal in grondgetallen:
        if getal > 0:
            resultaat = resultaat + getal**2
    return resultaat

print(kwadraten_som(lijst))
