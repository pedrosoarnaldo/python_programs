import pandas as pd
from pandas_datareader import data, wb
import datetime
import re
import os


class Stock:
    '''Class responsible to list the price and other information about stocks from around the world'''

    def __init__(self):
        symbol = '^GSPC' #	S&P 500
        company = 'yahoo'
        start = '2020-12-14'
        end = 'today'

    def getquote(self, symbol, company, start, end):
        return data.DataReader(symbol, company, start, end)

    def cleandata(self, dataframe):
        coll = []
        i = 0

        text_file = open("sample.tmp", "w")
        text_file.write(str(dataframe))
        text_file.close()

        for line in open('sample.tmp'):
            if re.search("^[0-9].*", line):
                i = i + 1
                coll.append({
                  'id': i,
                  'date': str(line).split()[0],
                  'high': str(line).split()[1],
                  'low': str(line).split()[2],
                  'volume': str(line).split()[4],
                  'close': str(line).split()[5]
                })

        os.remove('sample.tmp')
        return coll

    def groupdata(self, datacollection, piece):
        high = 0
        low = 0
        volume = 0
        close = 0
        coll = []

        if piece <= 1:
            return datacollection

        if len(datacollection) % piece > 0:
            print("Warning: The division in piece will return a non integer number.")

        for i in range(piece):
            high = float(datacollection[i]['high']) + high
            low = float(datacollection[i]['low']) + low
            volume = float(datacollection[i]['volume']) + volume
            close = float(datacollection[i]['close']) + close
            coll.append({'id': i+1, 'sum_high': high, 'sum_low': low, 'sum_volume': volume, 'sum_close': close})

        return coll

