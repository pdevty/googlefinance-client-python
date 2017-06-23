# googlefinance.client

googlefinance.client is a python client library for google finance api

## Installation

    $ pip install googlefinance.client

## Usage

```python
from googlefinance.client import get_price_data, get_closing_data, get_open_close_data, get_prices_data

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
# get closing price data (return pandas dataframe)
df = get_closing_data(params, period)
print(df)
#                 .DJI         NYA     .INX
# 2016-05-17  17710.71  10332.4261  2066.66
# 2016-05-18  17529.98  10257.6102  2047.21
# 2016-05-19  17526.62  10239.6501  2047.63
# 2016-05-20  17435.40  10192.5015  2040.04
# 2016-05-21  17500.94  10250.4961  2052.32
# ...              ...         ...      ...

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
# get open and close price data (return pandas dataframe)
df = get_open_close_data(params, period)
print(df)
#             .DJI_Open  .DJI_Close    NYA_Open   NYA_Close  .INX_Open  \
# 2016-06-21   17736.87    17804.87  10456.9207  10450.0288    2075.58   
# 2016-06-22   17827.33    17829.73  10481.1576  10490.7800    2085.19   
# 2016-06-23   17832.67    17780.83  10507.9429  10473.0578    2089.75   
# 2016-06-24   17844.11    18011.07  10573.4669  10641.1686    2092.80   
# 2016-06-25   17946.63    17400.75  10335.9189  10183.5145    2103.81   
# ...               ...         ...         ...         ...        ...   

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
# get open, high, low, close price data (return pandas dataframe)
df = get_prices_data(params, period)
print(df)
#            .DJI_Open .DJI_High  .DJI_Low .DJI_Close    NYA_Open    NYA_High  \
# 2016-06-24  17844.11  18011.07  17844.11   18011.07  10573.4669  10641.1704   
# 2016-06-25  17946.63  17946.63  17356.34   17400.75  10335.9189  10360.1025   
# 2016-06-28  17355.21  17355.21  17063.08   17140.24  10084.4835  10084.4835   
# 2016-06-29  17190.51  17409.72  17190.51   17409.72  10073.1527    10161.16   
# 2016-06-30  17456.02  17704.51  17456.02   17694.68  10254.8639  10362.0602   
# ...              ...       ...       ...        ...         ...         ...   
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request