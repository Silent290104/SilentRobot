import requests

from Silent.events import register


@register(pattern="[/!]dare")
async def dare(event):
    gay = requests.get("https://api.truthordarebot.xyz/v1/dare").json()
    dare = gay["question"]
    BOOB = "{}"
    await event.reply(BOOB.format(dare))


@register(pattern="[/!]truth")
async def truth(event):
    gae = requests.get("https://api.truthordarebot.xyz/v1/truth").json()
    truth = gae["question"]
    BOOB = "{}"

    await event.reply(BOOB.format(truth))
