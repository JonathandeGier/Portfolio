import datetime

b = 7

def verdubbelB():
    global b
    b = b + b


def f(y):
    return 2*y + 1

def g(x):
    return 5 + x + 10

verdubbelB()

print('code 1: {}'.format(b))

print('code 2: {}'.format(datetime.datetime.today().strftime("%H:%M:%S")))

print('code 3: {}'.format(f(3)+g(3)))

