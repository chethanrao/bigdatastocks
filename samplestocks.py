import urllib2
import time

stockToPull='GOOGL'

def pullData(stock):
    try:
	url='http://chartapi.finance.yahoo.com/instrument/1.0/'+stockToPull+'/chartdata;type=quote;range=1d/csv'
	data=urllib2.urlopen(url).read()
	print data
    except Exception,e:
	print 'main loop',str(e)


pullData(stockToPull)
