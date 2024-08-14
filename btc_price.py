import sys
import json
import requests
import os 
from gtts import gTTS
import platform


#Call coindesk API
try : 
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if r.status_code != 200 :
        sys.exit("Failed to recieve correct respond from API server!")
except : 
    sys.exit("Failed to recieve correct respond from API server!")


#Extract The Bitcoin price from response
data = json.loads(r.text)
btc_price = int(data["bpi"]["USD"]["rate_float"])
result = f"Bitcoin's current price is {btc_price:.2f} USD"


print(result)

#Saving the result as a mp3 file
tts = gTTS(text=result, lang='en')
tts.save("btc_price.mp3")

#Read result
os_name = platform.system()
if os_name == 'Windows':
    os.system("start btc_price.mp3")
elif os_name == 'Darwin':  # macOS
    os.system("afplay btc_price.mp3")
elif os_name == 'Linux':
    os.system("mpg123 btc_price.mp3")
else:
    print("Unsupported operating system for audio playback.")

