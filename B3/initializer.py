import DatabasePool

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

try:
    mongo = DatabasePool.DatabasePool()
    dbc = mongo.connect_mongo()
    mydb = dbc["stocks"]
    mycol = mydb["stockexchange"]
    mycol.insert_many(stocks)
    dbc.close()
    print('Collection stockexchange created.')
except:
    print('Error connecting to mongodb')





