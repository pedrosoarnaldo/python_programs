from stock import Stock

def analyzestock(stock, start, end, pieces):
    x = []
    y = []

    if stock is None:
        stocks = [
            {
                'symbol': '^NYA',
                'name': 'NYSE Composite',
                'country': 'EUA',
                'GMT': '-5'
            },
            {
                'symbol': '^IXIC',
                'name': 'NASDAQ Composite',
                'country': 'EUA',
                'GMT': '-5'
            },
            {
                'symbol': '^N225',
                'name': 'Nikkei 225',
                'country': 'JAP',
                'GMT': '+9'
            },
            {
                'symbol': '000001.SS',
                'name': 'Shangai - SSE Composite',
                'country': 'CHI',
                'GMT': '+8'
            },
            {
                'symbol': '^HSI',
                'name': 'Hong Kong - Hang Seng Index',
                'country': 'HKG',
                'GMT': '+8'
            },
            {
                'symbol': '^N100',
                'name': 'Euronext 100',
                'country': 'HOL',
                'GMT': '+1'
            },
            {
                'symbol': '^FTSE',
                'name': 'FTSE 100',
                'country': 'ING',
                'GMT': '+0'
            },
            {
                'symbol': '^GSPTSE',
                'name': 'Toronto Stock S&P/TSX Composite',
                'country': 'CAN',
                'GMT': '-5'
            },
            {
                'symbol': '^BSESN',
                'name': 'Bombay BSE',
                'country': 'IND',
                'GMT': '+5'
            },
            {
                'symbol': '^BVSP',
                'name': 'Ibovespa B3',
                'country': 'BRA',
                'GMT': '-3'
            }
        ]

        for symbol in stocks:
            print(symbol['name'])
            try:
                listdata(Stock(), symbol['symbol'], 'yahoo', start, end, pieces)
            except:
                print('Error obtaning ' + symbol['symbol'] + ' information')
    else:
        try:
            listdata(Stock(), stock, 'yahoo', start, end, pieces)
        except:
            print('Error obtaning ' + stock + ' information')


def listdata(c, symbol, finance, start, end, pieces):
    s = c.getquote(symbol, finance, start, end)
    cleandata = c.cleandata(s)
    groupby = c.groupdata(cleandata, pieces)
    print(groupby)


analyzestock(None, '2020-01-01', '2020-02-28', 4)

