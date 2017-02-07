import urllib.request
import json
import os

def direction(x):
    if x > 0:
        return "↗"
    elif x < 0:
        return "↘"
    else:
        return "→"

response = urllib.request.urlopen("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,LTC,ETH,XMR,MAID,DASH,EDR,ZEC,NXT,XRP&tsyms=USD")
try:
    data = json.loads(str(response.read(), 'utf-8'))
except:
    print(response.read())

if os.path.exists("oldvalues.json"):
    with open("oldvalues.json", "r") as f:
        olddata = json.loads(f.read())
else:
    olddata = data.copy()

for key, value in sorted(data.items()):
    print(key, direction(value["USD"]-olddata[key]["USD"]), value["USD"])

with open("oldvalues.json", "w") as f:
    f.write(json.dumps(data))
