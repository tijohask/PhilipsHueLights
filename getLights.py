# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.140/api/[USERNAME]/lights
# curl http://192.168.2.105/api/[USERNAME]/lights [-X POST]

import requests
import json

url = requests.get("https://www.meethue.com/api/nupnp").text
urldata = json.loads(url)
address = urldata[0]["internalipaddress"]

f = open("Username.txt", "r")
f.readline()
username = f.readline().rstrip()
f.close()

print( "http://" + address + "/api/" + username + "/lights" )
address = "http://" + address + "/api/" + username + "/lights"
# req = requests.post(address, json=data)
# req = requests.put(address, json=NewData)
req = requests.get(address)
print( req.text )


