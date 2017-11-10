def ticker(filename):
    tickers = open(filename)
    tickerlist = tickers.readlines()
    tickers.close()

    tickerd = dict()
    for ticker in tickerlist:
        tickercorp = ticker.split(':')
        tickerd[tickercorp[0]] = tickercorp[1]

    return tickerd

file = '../Files/ticker_symbols'

choice = int(input('Do you want to know the (1) Company name or (2) Ticker name: '))

if choice == 1:
    tickerdictionairy = ticker(file)
    tickername = input('Enter Ticker symbol: ')



elif choice == 2:
    dddeeded
else:
    print('Invalid, try again')