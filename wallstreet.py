import urllib.request
import json
import os
import discord

def direction(x):
    if x > 0:
        return "↗"
    elif x < 0:
        return "↘"
    else:
        return "→"

def querynumbers():
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

    result = ""
    for key, value in sorted(data.items()):
        result += "{0} {1} {2}\n".format(key, direction(value["USD"]-olddata[key]["USD"]), value["USD"])

    with open("oldvalues.json", "w") as f:
        f.write(json.dumps(data))

    return result


discordclient = discord.Client()

@discordclient.event
@asyncio.coroutine
def on_message(message):
    if discordclient.user.mention in message.content and not message.author.bot and message.channel == "#wallstreet":
        try:
            yield from discordclient.send_message(message.channel, querynumbers())
        except discord.errors.Forbidden:
            pass
