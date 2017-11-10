lange_lijst = eval(input("Geef lijst met minimaal 10 strings: "))
vier_letter_lijst = []

if len(lange_lijst) > 9:
    for woord in lange_lijst:
        if len(woord) == 4:
            vier_letter_lijst = vier_letter_lijst + [woord]
else:
    print('De lijst is niet lang genoeg!')

print(vier_letter_lijst)