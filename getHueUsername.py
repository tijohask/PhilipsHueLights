# Command Line HTTP:
# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.105/api/[USERNAME]/lights

import requests

url = requests.get( "https://www.meethue.com/api/nupnp" ).text
urldata = json.loads( url )
address = urldata[0]["internalipaddress"]

address = "http://" + address + "/api"

data = {"devicetype": "Light Control#Laptop"}

req = requests.post(address, json=data)
# req = requests.put(address, json=NewData)
# req = requests.get(address)


print req.text
