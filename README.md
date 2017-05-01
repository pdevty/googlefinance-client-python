# googlefinance.client

googlefinance.client is a python client library for google finance.

## Installation

execute:

    $ pip install googlefinance.client

## Usage

```python
from googlefinance.client import getprices
from datetime import datetime

query = {
	'q': "7203",	# Stock symbol (ex: "AAPL")
	'i': "86400",	# Interval size in seconds ("86400" = 1 day intervals)
	'x': "TYO",	# Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y",	# Period (Ex: "1Y" = 1 year)
	'ts': datetime.now().timestamp()	# Starting timestamp (Unix format). If blank, it uses today.
}
df = getprices(query)	# return pandas dataframe
print(df)
#                     DATE CLOSE  HIGH   LOW  OPEN    VOLUME
# 0    2016/05/02 15:00:00  5442  5468  5375  5404  12275800
# 1    2016/05/06 15:00:00  5478  5527  5418  5496   8986000
# 2    2016/05/09 15:00:00  5554  5575  5501  5528   7481300
# 3    2016/05/10 15:00:00  5677  5693  5516  5600   9782500
# 4    2016/05/11 15:00:00  5634  5776  5626  5716   8838100
# 5    2016/05/12 15:00:00  5553  5593  5380  5380  18599200
# ..                   ...   ...   ...   ...   ...       ...
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request