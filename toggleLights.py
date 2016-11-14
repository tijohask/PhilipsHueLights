# curl http://ex.am.p.le [-X [POST][PUT]]
# curl http://192.168.2.105/api/[USERNAME]/lights
# curl http://192.168.2.105/api/[USERNAME]/lights [-X POST]

import requests

address = "http://192.168.2.105/api/"

f = open("Username.txt", "r")
f.readline()
username = f.readline().rstrip()
f.close()

print( address + username + "/lights" )

# req = requests.post(address, json=data)
# req = requests.put(address, json=NewData)
# req = requests.get(address)



