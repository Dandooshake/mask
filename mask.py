import requests
import json
url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"

for i in range(1,55):
    r=requests.get(url+"/stores/json?page="+str(i))
    stores=json.loads(r.text)['storeInfos']
    for s in stores:
        if("광명시" in s["addr"]): print(s)
        if("서대문구" in s["addr"]): print(s)
        