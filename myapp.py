import yfinance as yf
import streamlit as st 
import pandas as pd 

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickersymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickersymbol)
# get the historical prices for this ticker 
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High     Low Case    Volume      Dividends       Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDF.Volume)
