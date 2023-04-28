import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

This app uses the data from the yfinance python module.

Created based on the following:
- Data professor tutorial: https://www.youtube.com/watch?v=JwSS70SZdyM&t=824s 
- Analysing Alpha's yfinance Python Tutorial (2023): https://analyzingalpha.com/yfinance-python#Who_Created_yFinance

Disclaimer: **DO NOT** use for making live trading decisions. This project was created purely for academic purposes.

""")

with st.sidebar:
    tickerSymbol = st.text_input('Enter the ticker of the company you would like to see the data for: ')
    period = st.selectbox('Period:', ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    start = st.date_input('Start date:')
    end = st.date_input('End date:')
    interval = st.selectbox('Interval:',
                            ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])
    graphs = st.multiselect('Choose the graphs you would like to see:', ['Close prices', 'Volume'])

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period=period, start=start, end=end, interval=interval)


def download_csv_data(df, ticker_symbol):
    # Download data as a CSV
    csv = df.to_csv().encode('utf-8')
    st.download_button(
        label="Download RAW data selection as CSV",
        data=csv,
        file_name=f'{ticker_symbol}_data.csv',
        mime='text/csv',
    )


# TODO: Troubleshoot graphs appearing based on selection and test download CSV functionality
if graphs == 'Close prices':
    st.write("""
    ## Close prices
    """)
    st.line_chart(tickerDf.Close)
    download_csv_data(tickerDf, tickerSymbol)
elif graphs == 'Volume':
    st.write("""
    ## Volume
    """)
    st.line_chart(tickerDf.Volume)
    download_csv_data(tickerDf, tickerSymbol)
