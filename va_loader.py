# Python 3
import http.client, urllib.parse

conn = http.client.HTTPConnection('api.positionstack.com')

params = urllib.parse.urlencode({
    'access_key': '2360d87c7defdf8a62f626f60cac8a65',
    'query': '146 Brandywine Ct Charlottesville',
    'region': 'Virginia',
    'limit': 1,
    })

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
data = res.read()

addresses_list = [
    
]

def get_geo_data(addresses):
    conn = http.client.HTTPConnection('api.positionstack.com')

    for address in addresses:
        params = urllib.parse.urlencode({
            'access_key': '2360d87c7defdf8a62f626f60cac8a65',
            'query': f'{address}',
            'region': 'Virginia',
            'limit': 1,
            })
        
        conn.request('GET', '/v1/forward?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        address_object =  {
                    "address1": f"{address}",
                    "address2": "",
                    "city": "Washington",
                    "state": "DC",
                    "postalCode": "20020",
                    "coordinates": {
                        "lat": data[0]['latitude'],
                        "lng": data[0]['latitude']
                    }
                }
        addresses_list.append(address_object)




print(data.decode('utf-8'))