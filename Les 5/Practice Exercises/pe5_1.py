temp = float(input('Temperatuur in Celsius: '))

def convert(tempCelsius):
    tempFahr = tempCelsius * 1.8 + 32
    return tempFahr

def table():
    print('   F       C')
    for temp in range(-30, 41, 10):
        fahr = temp * 1.8 + 32
        print('{:5}   {:5}'.format(fahr, float(temp)))
    return



print('Temperatuur in Fahrenheit: ' + str(convert(temp)))
table()