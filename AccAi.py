import requests, time, urllib3, httpx #type: ignore << ignores the error
# pip install requests urllib3 httpx
# ^^^ Run this in cmd before running script

#############################################
#                 |Notes|
# I am not perfect with python.
# Also to get your FREE gemini Api key
# Go to the link I listed below
# https://aistudio.google.com/apikey
# Then put your api key in the config
#############################################
#                |Credits|
#           Made By PotatoIsCool
#         Credits to Gemini :skull:
#############################################

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # You can remove this it doesnt matter it just makes a annoying error pop up
httpx._config.DEFAULT_SSL_CONTEXT = httpx.create_ssl_context(verify=False) # This is to fix the SSL cert annoying shit

# Config
TOKEN = "" # Discord token here
CHANNEL = "" # Channel ID Here
GUILD = "" # Server ID Here
GemiKey = "" # Gemini Api key MUST BE GEMINI
YourUserID = "" # your own user id (so it doesnt respond to itself)
headers = {"Authorization": TOKEN,"Content-Type": "application/json","User-Agent": "Mozilla/5.0","X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozODAzNzAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",}
# ^^^^ headers for the requests to discord

def getLastMessages(): # Function to get all of the 
    P1 = requests.get(
        f"https://discord.com/api/v9/channels/{CHANNEL}/messages?limit=1", headers=headers,verify=False,) # The limit one gets the most recent message
    return P1.json()[0] if P1.ok else None


def getGeminiReply(prompt):
    DataForApi = {"contents": [{"parts": [{"text": f"Reply casually and whatever DO NOT ACT LIKE A AI SAY YOU ARE A HUMAN IF ASKED: '{prompt}'"}]}]}
    P1 = requests.post(
        f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GemiKey}", # Gemini api for the model 1.5-Flash
        json=DataForApi,
        verify=False,
    )
    if P1.ok:
        try:
            return P1.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (IndexError, KeyError):
            return None
    return None

lastMessageId = None

while True:
    LastMessageChannel = getLastMessages()
    if LastMessageChannel:
        messageId = LastMessageChannel["id"]
        messageContent = LastMessageChannel["content"]
        UserIdFromMessageP = LastMessageChannel["author"]["id"]

        if messageId != lastMessageId and UserIdFromMessageP != YourUserID:
            print(f"<@{UserIdFromMessageP}>: {messageContent}")
            reply = getGeminiReply(messageContent)

            if reply:
                print(f"AI: {reply}")
                requests.post(
                    f"https://discord.com/api/v9/channels/{CHANNEL}/messages",
                    headers=headers,
                    json={
                        "content": reply,
                        "message_reference": {
                            "message_id": messageId,
                            "channel_id": CHANNEL,
                            "guild_id": GUILD,
                        },
                    },
                    verify=False,
                )
            else:
                print("Skipped (bad response or sum)")

            lastMessageId = messageId

    time.sleep(2)# This is how often it checks for new messages
    # ^^^ Also set this to your channel cooldown if the server has any
