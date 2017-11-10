a = 0
b = 0
c = 3
d = 4
e = 0

import math

def hit(cx, cy, c, px, py):
    resultaat = math.sqrt((cx - px)**2 + (cy - py)**2 ) <= c
    return resultaat

raak = hit(a, b, c, d, e)
print(raak)
