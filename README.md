# googlefinance.client

googlefinance.client is a python client library for google finance api

## Installation

    $ pip install googlefinance.client

## Usage

```python
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

# Dow Jones
param = {
	'q': ".DJI", # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "INDEXDJX", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
}
# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)
#                          Open      High       Low     Close     Volume
# 2016-05-17 05:00:00  17531.76   17755.8  17531.76  17710.71   88436105
# 2016-05-18 05:00:00  17701.46  17701.46  17469.92  17529.98  103253947
# 2016-05-19 05:00:00  17501.28  17636.22  17418.21  17526.62   79038923
# 2016-05-20 05:00:00  17514.16  17514.16  17331.07   17435.4   95531058
# 2016-05-21 05:00:00  17437.32  17571.75  17437.32  17500.94  111992332
# ...                       ...       ...       ...       ...        ...

params = [
	# Dow Jones
	{
		'q': ".DJI",
		'x': "INDEXDJX",
	},
	# NYSE COMPOSITE (DJ)
	{
		'q': "NYA",
		'x': "INDEXNYSEGIS",
	},
	# S&P 500
	{
		'q': ".INX",
		'x': "INDEXSP",
	}
]
period = "1Y"
# get open, high, low, close, volume data (return pandas dataframe)
df = get_prices_data(params, period)
print(df)
#            .DJI_Open  .DJI_High  .DJI_Low  .DJI_Close  .DJI_Volume  \
# 2016-07-20   18503.12   18562.53  18495.11    18559.01    85840786   
# 2016-07-21   18582.70   18622.01  18555.65    18595.03    93233337   
# 2016-07-22   18589.96   18590.44  18469.67    18517.23    86803016   
# 2016-07-23   18524.15   18571.30  18491.59    18570.85    87706622   
# 2016-07-26   18554.49   18555.69  18452.62    18493.06    76807470   
# ...               ...        ...       ...         ...         ...   

params = [
	# Dow Jones
	{
		'q': ".DJI",
		'x': "INDEXDJX",
	},
	# NYSE COMPOSITE (DJ)
	{
		'q': "NYA",
		'x': "INDEXNYSEGIS",
	},
	# S&P 500
	{
		'q': ".INX",
		'x': "INDEXSP",
	}
]
period = "1Y"
interval = 60*30 # 30 minutes
# get open, high, low, close, volume time data (return pandas dataframe)
df = get_prices_time_data(params, period, interval)
print(df)
#                      .DJI_Open  .DJI_High  .DJI_Low  .DJI_Close  .DJI_Volume  \
# 2016-07-19 23:00:00   18503.12   18542.13  18495.11    18522.47            0   
# 2016-07-19 23:30:00   18522.44   18553.30  18509.25    18546.27            0   
# 2016-07-20 00:00:00   18546.20   18549.59  18519.77    18539.93            0   
# 2016-07-20 00:30:00   18540.24   18549.80  18526.99    18534.18            0   
# 2016-07-20 01:00:00   18534.05   18540.38  18507.34    18516.41            0   
# ...                        ...        ...       ...         ...          ...   
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request