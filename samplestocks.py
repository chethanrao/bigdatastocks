import urllib2

stockToPull='GOOGL'

def pullData(stock):
	url='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1d/csv'
	data=urllib2.urlopen(url).read()
	lines=data.split("\n")
	for line in lines:
		firstString=line.split(",")[0]
		#print firstString
		if isfloat(firstString) or isint(firstString):
			print line

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isint(value):
  try:
	int(value)
	return True
  except ValueError:
	return False
pullData(stockToPull)
