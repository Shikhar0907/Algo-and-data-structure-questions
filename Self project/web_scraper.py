import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates as mdates
import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
style.use('ggplot')
##
##start = dt.datetime(2013,1,1)
##end = dt.datetime.today()
##df = pdr.get_data_yahoo("AAPL",start,end)

##df.to_csv("Apple.csv")

df =pd.read_csv("Apple.csv", parse_dates = True, index_col = 0)

##print(df.head())

##df.plot()
##plt.show()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head())


ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan = 1,colspan = 1, sharex = ax1)

##ax1.plot(df.index,df['Adj Close'])
##ax1.plot(df.index, df['100ma'])
##ax2.plot(df.index, df['Volume'])

##plt.show()
##
