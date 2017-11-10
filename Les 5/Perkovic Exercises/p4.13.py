s = 'abcdefghijklmnopqrstuvwxyz'

a = s[1:3] in 'bc'
b = s[:14] in 'abcdefghijklmn'
c = s[:14] not in 'opqrstuvwxyz'
d = s[1:len(s) -1] == 'bcdefghijklmnopqrstuvw'

print(a, b, c, d)