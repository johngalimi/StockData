import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt

ticker = 'HD'
years_back = 3
months_back = 0

ma_window_1 = 30
ma_window_2 = 90

plt.style.use('ggplot')

today = datetime.now()
start = datetime(today.year - years_back,
                 today.month - months_back, today.day)
end = datetime(today.year, today.month, today.day)

df = web.DataReader(ticker, 'iex', start, end)
df = df[['close', 'volume']]

df.index = pd.to_datetime(df.index)

fig = plt.figure()

ax1 = plt.subplot2grid((4, 4), (0, 0), colspan=4, rowspan=3)

plt.title(ticker + ': ' + str(start).split()[0] + ' to Present', fontsize=20)
plt.ylabel('Closing Price (USD)', fontsize=14)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)

last_date = df.index[-1]
last_price = df['close'][-1]

ax2 = plt.subplot2grid((4, 4), (3, 0), colspan=4, sharex=ax1)

plt.ylabel('Volume (bn)', fontsize=14)
plt.xticks(fontsize=12)
plt.xlabel('Date', fontsize=14)

ax1.plot(df.index, df['close'], lw=2, label='Price')
ax1.plot(df.index, df['close'].rolling(window=ma_window_1).mean(), lw=2, 
         label= str(ma_window_1) + 'ma')
ax1.plot(df.index, df['close'].rolling(window=ma_window_2).mean(), lw=2, 
         label= str(ma_window_2) + 'ma')

ax1.legend()

ax2.bar(df.index, df['volume'])

plt.legend()

plt.tight_layout()
plt.show()
