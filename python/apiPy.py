#package is used for api things 'requests'
#json library is used format the json data

import json
import requests
import sys

if len(sys.argv) != 2 :
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#response is a string which stores the json response sent by the site
#print(response)
#nt(json.dumps(response.json(),indent=2)) #prints the data in json format

obj = response.json()
for result in obj["results"] :
    print(result["trackName"])