# coding: utf-8

import requests
from datetime import datetime, timedelta
import pandas as pd

def getprices(query):
	r = requests.get("https://www.google.com/finance/getprices", params=query)
	lines = r.text.splitlines()
	columns = lines[4].split("=")[1].split(",")
	prices = lines[8:]
	result = []
	base = 0
	for price in prices:
		cols = price.split(",")
		if cols[0][0] == 'a':
			base = datetime.fromtimestamp(int(cols[0][1:]))
			date = base
		else:
			date = base + timedelta(int(cols[0]))
		result.append([date.strftime("%Y/%m/%d %H:%M:%S"), cols[1], cols[2], cols[3], cols[4], cols[5]])
	return pd.DataFrame(result, columns = columns)

if __name__ == '__main__':
	query = {
		'q': "7203",
		'i': "86400",
		'x': "TYO",
		'p': "1Y",
		'ts': datetime.now().timestamp()
	}
	df = getprices(query)
	print(df)