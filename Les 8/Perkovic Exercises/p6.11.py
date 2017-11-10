def easyCrypto(string):
    encryptedstring = str()

    for char in string:
        getal = ord(char)
        if getal % 2 == 0:
            getal -= 1
            encryptedstring += chr(getal)
        else:
            getal += 1
            encryptedstring += chr(getal)

    return encryptedstring

userstring = input('Typ een string die je wilt encrypten: ')

print('De encrypted string: {}'.format(easyCrypto(userstring)))