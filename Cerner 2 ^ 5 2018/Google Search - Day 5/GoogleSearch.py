# cerner_2^5_2018

import urllib
import json as j
import urllib.parse
import urllib.request

query = input( 'Search for something: ' )
query = urllib.parse.urlencode ( { 'q' : query } )
response = urllib.request.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
json = j.loads ( response )
results = json [ 'responseData' ] [ 'results' ]
for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )