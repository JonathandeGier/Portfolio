sa = '10 20 30 40 50 60'
sb = '10,20,30,40,50,60'
sc = '10&20&30&40&50&60'
sd = '10 - 20 - 30 - 40 - 50 - 60'

a = sa.split()
b = sb.split(',')
c = sc.split('&')
d = sd.split(' - ')

print(a)
print(b)
print(c)
print(d)