import pandas as pd

mydataframe = pd.read_csv('DADOS/microdados_750k.csv', sep=";", encoding="ISO-8859-1")

### Listing all the columns of the dataframe
#print(mydataframe.columns.values)

y = mydataframe[0:100]

print(y.columns.values)