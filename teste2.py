import yfinance as yf
import pandas as pd


bb = yf.download(tickers="BBAS3.SA", start="2022-01-01", end="2025-06-01", interval="1d")

print(bb.head())