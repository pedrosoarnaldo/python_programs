import pandas as pd
from pandas_datareader import data, wb

import datetime
start = pd.to_datetime('2020-12-10')
end = pd.to_datetime('today')

### Nasdaq
stock = data.DataReader('^IXIC', 'yahoo', start, end)
print(stock)
