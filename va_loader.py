# Python 3
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

params = urllib.parse.urlencode({
    'access_key': '2360d87c7defdf8a62f626f60cac8a65',
    'query': '4400 Cox Rd #200 Glen Allen',
    'region': 'Virginia',
    'limit': 1,
    })

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))