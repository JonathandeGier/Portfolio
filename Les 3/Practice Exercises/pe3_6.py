s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = 'aeiou'

for letter in s:
    for klinker in klinkers:
        if letter == klinker:
            print(letter)