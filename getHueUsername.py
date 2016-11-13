# Command Line HTTP:
# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.105/api/[USERNAME]/lights

import requests

address = "http://192.168.2.105/api"

data = {"devicetype": "Light Control#Laptop"}

req = requests.post(address, json=data)
# req = requests.put(address, json=NewData)
# req = requests.get(address)


print req.text
