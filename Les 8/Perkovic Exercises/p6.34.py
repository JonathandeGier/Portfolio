import random

def game(aantalvragen):
    aantalgoedeantwoorden = 0
    for vraag in range(aantalvragen):
        getal1 = random.randrange(1,10)
        getal2 = random.randrange(1,10)

        print('{} + {} ='.format(getal1, getal2))
        antwoord = int(input('Enter answer: '))

        if getal1 + getal2 == antwoord:
            print('Correct.')
            aantalgoedeantwoorden += 1
        else:
            print('Incorrect.')

    print('You got {} correct answers out of {}'.format(aantalgoedeantwoorden, aantalvragen))

aantalvragen = int(input('Hoeveel vragen wil je: '))

game(aantalvragen)