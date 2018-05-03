import pandas as pd
from pandas import DataFrame
import datetime

start = datetime.datetime(2016, 10, 1)
end = datetime.datetime(2017, 1, 31)

import pandas_datareader.data as web

start = datetime.datetime(2010, 1, 1)

end = datetime.datetime(2013, 1, 27)

# apple = web.DataReader('F', 'google', start, end)
apple = web.DataReader('F', 'morningstar', start, end)

print(apple.head())
apple.to_csv('apple-data.csv')
df = pd.read_csv('apple-data.csv', index_col='Date', parse_dates=True)
df.head()