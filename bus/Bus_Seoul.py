from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'nuD0VA4oaDhlyilVJNYSxhuI8x23SqQQN2kHmPkbklAUhhLmy0UioY92z6yQtx0oCLl6DlNrk%2FkTwkkHhwfvcA%3D%3D', quote_plus('stId') : '22274', quote_plus('busRouteId') : '3412', quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body

# def call:
# 	return "call api"

