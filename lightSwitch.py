# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.140/api/[USERNAME]/lights
# curl http://192.168.2.105/api/[USERNAME]/lights [-X POST]

import requests
import json

# Get the current ip address of the bridge
url = requests.get( "https://www.meethue.com/api/nupnp" ).text
urldata = json.loads( url )
ip = urldata[0]["internalipaddress"]

# Get the username of the current device
f = open( "Username.txt", "r" )
f.readline()
username = f.readline().rstrip()
f.close()

# Put together the address, convert the resultant text to a json object
address = "http://" + ip + "/api/" + username + "/lights/"
req = requests.get( address )
data = json.loads( req.text )

# Do stuff based on the json object
for item in data:
	req = requests.put( address + item + "/state", json={"bri":254,"on":True} )
	print( req.text )
	

