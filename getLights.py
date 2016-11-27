# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.140/api/[USERNAME]/lights
# curl http://192.168.2.105/api/[USERNAME]/lights [-X POST]

import requests
import json

url = requests.get( "https://www.meethue.com/api/nupnp" ).text
# [{"id":"001788fffe222a8f","internalipaddress":"192.168.2.140"}]
urldata = json.loads( url )
address = urldata[0]["internalipaddress"]

f = open( "Username.txt", "r" )
f.readline()
username = f.readline().rstrip()
f.close()

#print( "http://" + address + "/api/" + username + "/lights/" )
address = "http://" + address + "/api/" + username + "/lights/"

req = requests.get( address )
data = json.loads( req.text )
print( json.dumps( data, indent=4, sort_keys=True ) )

for item in data:
	print( )
	print( data[item]["name"] )
	print( "Reachable: " + str( data[item]["state"]["reachable"] ) )
	print( "On: " + str( data[item]["state"]["on"] ) )

#if( data["5"]["state"]["on"] ):
#	print("True")
