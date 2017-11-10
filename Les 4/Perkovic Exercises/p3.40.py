lst = eval(input('Zet hier de lijst met cijfers: '))

print(lst)
for student in lst:
    gem = sum(lst[student]) / len(lst[student])
    print(gem)
