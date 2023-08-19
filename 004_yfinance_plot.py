#   - To get Yahoo finance library
#     $ pip install yfinance

>>> import yfinance as yf
>>> ticker_symbol = 'AAPL'
>>> ticker_data = yf.Ticker(ticker_symbol)
>>> hist_data = ticker_data.history(period='1d', start='2020-01-01', end='2023-01-01')
>>> hist_data
                                 Open        High         Low       Close     Volume  Dividends  Stock Splits
Date
2020-01-02 00:00:00-05:00   72.246670   73.309986   71.990600   73.249016  135480400        0.0           0.0
2020-01-03 00:00:00-05:00   72.468602   73.305105   72.310083   72.536888  146322800        0.0           0.0
2020-01-06 00:00:00-05:00   71.649184   73.153913   71.395548   73.114891  118387200        0.0           0.0

>>> type(hist_data)
<class 'pandas.core.frame.DataFrame'>

>>> import matplotlib.pyplot as plt
>>> closing_prices = hist_data['Close']
>>> plt.plot(closing_prices)
[<matplotlib.lines.Line2D object at 0x000001833DD3C490>]
>>> plt.title('Apple Inc. (AAPL) Closing Prices')
Text(0.5, 1.0, 'Apple Inc. (AAPL) Closing Prices')
>>> plt.xlabel('Date')
Text(0.5, 0, 'Date')
>>> plt.ylabel('Closing Price (USD)')
Text(0, 0.5, 'Closing Price (USD)')
>>> plt.show()
>>>
