def hexASCII():
    for letter in range(ord('a'), ord('z') + 1):
        char = chr(letter)
        hexletter = hex(letter)
        hexletter = hexletter.replace('0x', '')
        print('{}:{}'.format(char, hexletter), end=" ")

hexASCII()