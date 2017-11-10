def code(invoerstring):
    outputstring = str()
    for char in invoerstring:
        letter = ord(char)
        letter += 3
        outputstring += chr(letter)
    return outputstring

naam = input('Naam: ')
beginstation = input('Beginstation: ')
eindstation = input('Eindstation: ')

string = naam + beginstation + eindstation

print(code(string))