import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = st.text_input('Enter the ticker of the company you would like to see the data for: ')
period = st.selectbox('Period:', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
start = st.date_input('Start date:')
end = st.date_input('End date:')
interval = st.selectbox('Interval:', ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period=period, start=start, end=end, interval=interval)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

