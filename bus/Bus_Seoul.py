# from urllib2 import Request, urlopen
# from urllib import urlencode, quote_plus

# url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'
# queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('stId') : '', quote_plus('busRouteId') : '', quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })

# request = Request(url + queryParams)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print response_body

def call:
	return "call api"

