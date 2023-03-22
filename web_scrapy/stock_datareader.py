from pandas_datareader import data as pdr
from datetime import datetime
import yfinance as yf

yf.pdr_override()
# y_symbols = ['SCHAND.NS', 'TATAPOWER.NS', 'ITC.NS']

y_symbols = ['AAPL', 'MSFT']
from datetime import datetime
startdate = datetime(2022,1,1)
enddate = datetime(2023,3,5)
data = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)
