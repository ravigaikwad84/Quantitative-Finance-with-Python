#!/usr/bin/env python
# coding: utf-8

# # Outline

# #How to import financial data using Pandas DataReader and yfinance libraries. 
# #Understanding financial notations and definitions. 
# #Familiarity with the OHLC notation.
# #How to plot candlestick charts using mpl_finance library. 
# #Importance of financial indicators and implemented some of them using the stockstats library.

# In[1]:


pip install pandas-datareader yfinance mpl-finance stockstats


# # import AAPL stock price
# 
# 

# In[5]:



import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[7]:



df_aapl = pdr.get_data_yahoo("AAPL", start="2019-01-01", end="2019-09-30")


# In[8]:


df_aapl.head()


# A candle in financial market is presented under the format OHLC which stands for "Open-High-Low-Close":
# 
# Open: is the price of a stock when a time resolution started (1m, 30m, hourly, daily, etc)
# High: is the highest price reached from the beginning to the end of candle.
# Low: is the lowest price reached from the beginning to the end of candle.
# Close: is the price of a stock when a time resolution finishes.
# 
# Two types of trading operations in the financial stock markets:
# Long (Buy)
# Short (Sell).

# In[15]:


pip install mplfinance 


# # Plotting Stock Prices
# 

# In this section, we will use matplotlib and mpl_finance libraries to plot the stock prices of AAPL. First, we will plot the Open-High-Low-Close prices separately:
# 
# 

# In[49]:


df_aapl[["Open", "High", "Low", "Close"]].plot()
plt.show()


# In[19]:


len(df_aapl)


# In[50]:


fig = plt.figure(figsize=(10, 10))
ax = plt.subplot()

plot_data = []
for i in range(150, len(df_aapl)):
    row = [
        i, 
        df_aapl.Open.iloc[i], 
        df_aapl.High.iloc[i], 
        df_aapl.Low.iloc[i], 
        df_aapl.Close.iloc[i], 
    ]
    plot_data.append(row)
candlestick_ohlc(ax, plot_data)
plt.show()


# candle-structure.png![image.png](attachment:image.png)
# 

# From the stockstats library we will import StockDataFrame, which is a class that receives as an attribute a pandas DataFrame sorted by time and includes the columns Open-Close-High-Low in this order:

# In[21]:


from stockstats import StockDataFrame

stocks = StockDataFrame.retype(df_aapl[["Open", "Close", "High", "Low", "Volume"]])


# # SIMPLE MOVING AVERAGE(SMA)

# Simple Moving Average is an indicator which smoothens the stock prices plot, by computing the mean of the prices over a period of time. This will allow us to better visualize the trends directions (up or down)

# ![image.png](attachment:image.png)
# 

# In[38]:


plt.plot(figsize=(10,15))
            
plt.plot(stocks["close_10_sma"], color="b", label="SMA")
plt.plot(df_aapl.Close, color="g", label="Close prices")
plt.legend(loc="lower right")
plt.show()


# # Exponential Moving Average (EMA)

# Unlike the SMA, which gives equal weights to all prices whether the old or new ones, the Exponential Moving Average emphasizes on the last (most recent) prices by attributing to them a greater weight, this makes the EMA an indicator which detects trends faster than the SMA.

# # ![image.png](attachment:image.png)

# In[45]:


get_ipython().run_line_magic('matplotlib', 'inline')
import mpld3
mpld3.enable_notebook()


# In[47]:



plt.plot(figsize=(100,100))
plt.plot(stocks["close_10_sma"], color="b", label="SMA") # plotting SMA
plt.plot(stocks["close_10_ema"], color="k", label="EMA")#plotting EMA
plt.plot(df_aapl.Close, color="g", label="Close prices") # plotting close prices
plt.legend(loc="lower right")
plt.show()# mouse zooming


# In the zoom figure, we can clearly observe that indeed EMA responds faster to the change of trends and gets closer to them.
# 
# 

# # Moving Average Convergence/Divergence (MACD)
# 

# Moving Average Convergence/Divergence is a trend-following momentum indicator. This Indicator can show changes in the speed of price movement and traders use it to determine the direction of a trend. 
# 
# The MACD is calculated by subtracting the 26-period Exponential Moving Average (EMA) from the 12-period EMA. A nine-day EMA of the MACD is called “Signal Line”, which is then plotted with the MACD. 
# 
# When MACD crosses below the Signal Line it is an indicator to start doing short (Sell) operations. And when it crosses above it, it is an indicator to start doing long (Buy) operations:
# 
# When the MACD line is above the signal line, then the histogram will be positive.
# 
# 

# ![image.png](attachment:image.png)

# In[48]:


plt.plot(stocks["macd"], color="b", label="MACD")
plt.plot(stocks["macds"], color="g", label="Signal Line")
plt.legend(loc="lower right")
plt.show()


# In[ ]:





# In[ ]:




