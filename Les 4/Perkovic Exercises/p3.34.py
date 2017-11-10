nummer = int(input('Nummer: '))

def reverse_int(integer):
    resultaat = int()
    index2 = (integer % 10)
    index1 = ((integer % 100) - index2)
    index2 = index2 * 100
    index0 = integer // 100
    resultaat = index0 + index1 + index2
    return resultaat

print(reverse_int(nummer))