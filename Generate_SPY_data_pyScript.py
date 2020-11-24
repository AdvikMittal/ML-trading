
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from IPython import get_ipython

# %% [markdown]
# ## Creating train and test data for a Decision Tree Classfier Model

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pandas_datareader import data as wb
import talib
get_ipython().run_line_magic('matplotlib', 'widget')


# %%
# Daily OLHCV data for the S&P 500 etf SPY
df1 = pd.DataFrame()
df1 = wb.DataReader('SPY', data_source='yahoo', start='2016-01-01')


# %%
# Daily OLHCV data for the S&P 500 etf SPY
df1 = pd.DataFrame()
df1 = wb.DataReader('SPY', data_source='yahoo', start='2016-01-01')

# Create dataframe with SPY daily close price
df = pd.DataFrame()
df['SPY'] = df1['Close']

# Compute and add indicators to the dataframe
df['pct_chg_1'] = df['SPY'].diff()
df['pct_chg_5'] = df['SPY'].diff(periods=5)
df['diffSPY'] = df['SPY'] - df['SPY'].rolling(window = 5).mean()
df['VIX'] = wb.DataReader('^VIX', data_source='yahoo', start='2016-01-01')['Close']
df['RSI_7'] = talib.RSI(df.iloc[:, 1].values, timeperiod=7)
df['RSI_14'] = talib.RSI(df.iloc[:, 1].values)
df['diffRSI'] = df['RSI_7'] - df['RSI_7'].rolling(window = 14).mean()
df['MFI_7'] = talib.MFI(df1['High'], df1['Low'], df1['Close'], df1['Volume'], timeperiod=7)
df['MFI_14'] = talib.MFI(df1['High'], df1['Low'], df1['Close'], df1['Volume'], timeperiod=14)
df['signal'] = 0


# %%
# Truncate NaN values created while computing indicators and reset to a numerical index
df = df[21:]
df = df.reset_index()


# %%
# Set buy signals when a day's close price is lower than the past 5 and next 5 days
def buy_signals():
    for i in range(5, len(df)-5):
        if df['SPY'][i] == df['SPY'][i-5:i+5].min():
            df.at[i, 'signal'] = 1
            i += 4

# Set sell signals at the highest close price between 2 subsequent buy signals
def sell_signals():
    for n in range(len(buys)-1):
        buy1 = buys[n]
        buy2 = buys[n+1]
        maxIdx = df.iloc[buy1:buy2]['SPY'].idxmax()
        df.at[maxIdx, 'signal'] = -1


# %%
# Generate buy and sell signals
buy_signals()
buys = df.index[df['signal'] == 1].tolist()
sell_signals()


# %%
plt.figure(figsize = (9,7))

# plot close price
df['SPY'].plot(color = 'k', label= 'Close Price') 

# plot buy prices
plt.plot(df[df['signal'] == 1].index, 
         df['SPY'][df['signal'] == 1], 
         '^', markersize = 6, color = 'lime', label = 'buy')

# plot sell prices
plt.plot(df[df['signal'] == -1].index, 
         df['SPY'][df['signal'] == -1], 
         'v', markersize = 6, color = 'r', label = 'sell')

plt.ylabel('Price in USD', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('SPY train and test data', fontsize = 20)
plt.legend()
plt.grid()
plt.show()


# %%
# Set Date as index
datetime_index = pd.DatetimeIndex(pd.to_datetime(df['Date']))
df = df.set_index(datetime_index)
df = df.drop(['Date'], axis=1)


# %%
df


# %%
# Output data as CSV
df.to_csv(r'SPY_train_test_data.csv')

