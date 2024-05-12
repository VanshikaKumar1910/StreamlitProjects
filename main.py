import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

start_date = st.date_input("Start date", pd.to_datetime('2010-05-31'))
end_date = st.date_input("End date", pd.to_datetime('2020-05-31'))

# Convert datetime objects to strings in the format 'YYYY-MM-DD'
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

tickerDf = tickerData.history(period='1d',
                              start=start_date_str,
                              end=end_date_str)

st.write("## Stock Closing Price")
st.line_chart(tickerDf['Close'])  # Corrected to use 'Close' column.

st.write("## Stock Volume")
st.line_chart(tickerDf['Volume'])  # Corrected to use 'Volume' column.

stats = tickerDf.describe()
st.write("## Stock Statistics")
st.write(stats)
