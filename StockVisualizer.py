import datetime as dt
import mplfinance as mpl
import pandas_datareader as web
import pandas as pd

startDate = dt.datetime(2022,1,1)
endDate = dt.datetime(2022,12,1)

company = 'TSLA'

df = web.DataReader(company,'yahoo',startDate,endDate)


mpl.plot(
    df,
    type="candle",
    mav = (3,6,9),
    title = f"{company} Stock Price",
    style = "binance"
)