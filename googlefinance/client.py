# coding: utf-8
import requests
from datetime import datetime
import pandas as pd

def get_price_data(query):
	r = requests.get("https://www.google.com/finance/getprices", params=query)
	lines = r.text.splitlines()
	data = []
	index = []
	basetime = 0
	for price in lines:
		cols = price.split(",")
		if cols[0][0] == 'a':
			basetime = int(cols[0][1:])
			index.append(datetime.fromtimestamp(basetime))
			data.append([cols[4], cols[2], cols[3], cols[1], cols[5]])
		elif cols[0][0].isdigit():
			date = basetime + (int(cols[0])*int(query['i']))
			index.append(datetime.fromtimestamp(date))
			data.append([cols[4], cols[2], cols[3], cols[1], cols[5]])
	return pd.DataFrame(data, index = index, columns = ['Open', 'High', 'Low', 'Close', 'Volume'])

def get_closing_data(queries, period):
	closing_data = []
	for query in queries:
		query['i'] = 86400
		query['p'] = period
		r = requests.get("https://www.google.com/finance/getprices", params=query)
		lines = r.text.splitlines()
		data = []
		index = []
		basetime = 0
		for price in lines:
			cols = price.split(",")
			if cols[0][0] == 'a':
				basetime = int(cols[0][1:])
				date = basetime
				data.append(float(cols[1]))
				index.append(datetime.fromtimestamp(date).date())
			elif cols[0][0].isdigit():
				date = basetime + (int(cols[0])*int(query['i']))
				data.append(float(cols[1]))
				index.append(datetime.fromtimestamp(date).date())
		s = pd.Series(data,index=index,name=query['q'])
		closing_data.append(s[~s.index.duplicated(keep='last')])
	return pd.concat(closing_data, axis=1)

def get_open_close_data(queries, period):
	open_close_data = pd.DataFrame()
	for query in queries:
		query['i'] = 86400
		query['p'] = period
		r = requests.get("https://www.google.com/finance/getprices", params=query)
		lines = r.text.splitlines()
		data = []
		index = []
		basetime = 0
		for price in lines:
			cols = price.split(",")
			if cols[0][0] == 'a':
				basetime = int(cols[0][1:])
				date = basetime
				data.append([float(cols[4]), float(cols[1])])
				index.append(datetime.fromtimestamp(date).date())
			elif cols[0][0].isdigit():
				date = basetime + (int(cols[0])*int(query['i']))
				data.append([float(cols[4]), float(cols[1])])
				index.append(datetime.fromtimestamp(date).date())
		df = pd.DataFrame(data, index=index, columns=[query['q']+'_Open',query['q']+'_Close'])
		open_close_data = pd.concat([open_close_data, df[~df.index.duplicated(keep='last')]], axis=1)
	return open_close_data


if __name__ == '__main__':
	# Dow Jones
	param = {
		'q': ".DJI",
		'i': "86400",
		'x': "INDEXDJX",
		'p': "1Y"
	}
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
	df = get_open_close_data(params, period)
	print(df)
	#             .DJI_Open  .DJI_Close    NYA_Open   NYA_Close  .INX_Open  \
	# 2016-06-21   17736.87    17804.87  10456.9207  10450.0288    2075.58   
	# 2016-06-22   17827.33    17829.73  10481.1576  10490.7800    2085.19   
	# 2016-06-23   17832.67    17780.83  10507.9429  10473.0578    2089.75   
	# 2016-06-24   17844.11    18011.07  10573.4669  10641.1686    2092.80   
	# 2016-06-25   17946.63    17400.75  10335.9189  10183.5145    2103.81   
	# ...               ...         ...         ...         ...        ...   
