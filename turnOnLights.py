# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.140/api/[USERNAME]/lights
# curl http://192.168.2.105/api/[USERNAME]/lights [-X POST]

import requests
import json

url = requests.get("https://www.meethue.com/api/nupnp").text
# [{"id":"001788fffe222a8f","internalipaddress":"192.168.2.140"}]
urldata = json.loads(url)
ip = urldata[0]["internalipaddress"]

f = open("Username.txt", "r")
f.readline()
username = f.readline().rstrip()
f.close()

address = "http://" + ip + "/api/" + username + "/lights/"
req = requests.get( address )
data = json.loads(req.text)

for item in data:
	req = requests.put( address + item + "/state", json={"bri":254,"on":True} )
	print( req.text )
	
#curl -H "Content-Type: application/json" -X PUT http://192.168.2.140/api/OVPZzgH9sqRkwht4etpDhrYNL1CCIsJ6Ry2MB3B0/lights/5/state -d '{"on":true}' 

