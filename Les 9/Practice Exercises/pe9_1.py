kosten = 4356

try:
    while True:
        aantal = int(input('met hoeveel mensen? '))
        if aantal < 0:
            print('Negatieve getallen zijn niet toegestaan!')
        else:
            break

    uitkomst = kosten / aantal
    print('Kosten per persoon: € {}'.format(uitkomst))
except ZeroDivisionError:
    print('Delen door nul kan niet!')
except ValueError:
    print('Gebruik cijfers voor het invoeren van het aantal!')
except:
    print('Onjuiste invoer!')