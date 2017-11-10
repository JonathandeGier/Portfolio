def inValues():
    inputnotzero = True
    som = 0
    errorsinarow = 0

    while inputnotzero:
        try:
            nummer = eval(input('Please enter a number: '))
            som += nummer
            errorsinarow = 0

            if nummer == 0:
                inputnotzero = False
                print(som)
        except TypeError:
            errorsinarow += 1
            print('Error. Please re-enter the value.')
            if errorsinarow == 2:
                print('Two errors in a row. Quitting ...')
                inputnotzero = False

inValues()