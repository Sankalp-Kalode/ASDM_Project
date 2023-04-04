# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:46:08 2022

@author: Sankalp Kalode
"""

import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Stock Finance Dashboard')

tickers = ('TSLA', 'AAPL', 'MSFT', 'BTC-USD', 'ETH-USD','TATASTEEL.NS', 'RELI', 'KPITTECH.NS', 'HAPPSTMNDS.NS', 'PAYTM.NS', 'TRIDENT.NS')

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value = pd.to_datetime('2022-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df = pd.DataFrame()
    df = yf.download(dropdown, start, end)['Adj Close']
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)









#def relativeret(df):
#    rel = df.pct_change()
#    cumret = (1+rel).cumprod() - 1
#    cumret = cumret.fillna(0)
#    return cumret



    #df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
