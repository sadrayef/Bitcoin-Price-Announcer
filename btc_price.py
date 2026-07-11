import time
import platform
import subprocess
import requests
from gtts import gTTS

API_URL = "https://api.coingecko.com/api/v3/simple/price"
OUTPUT_FILE = "btc_price.mp3"
INTERVAL = 300  # 5 minutes


def get_bitcoin_price():
    """Fetch the current Bitcoin price in USD."""

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["bitcoin"]["usd"]


def generate_audio(message):
    """Generate an MP3 containing the spoken message."""

    tts = gTTS(text=message, lang="en")
    tts.save(OUTPUT_FILE)


def play_audio():
    """Play the generated MP3 on the current operating system."""

    system = platform.system()

    if system == "Windows":
        subprocess.run(["start", OUTPUT_FILE], shell=True)

    elif system == "Darwin":
        subprocess.run(["afplay", OUTPUT_FILE])

    elif system == "Linux":
        subprocess.run(["mpg123", OUTPUT_FILE])

    else:
        print("Unsupported operating system.")


def main():
    print("Bitcoin Price Announcer started.")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            price = get_bitcoin_price()

            message = f"Bitcoin's current price is {price:,.2f} USD"

            print(message)

            generate_audio(message)
            play_audio()

            print(f"Next announcement in {INTERVAL // 60} minutes.\n")
            

            time.sleep(INTERVAL)

        except KeyboardInterrupt:
            print("\nBitcoin Price Announcer stopped.")
            break

        except requests.RequestException as e:
            print(f"Network error: {e}")
            time.sleep(30)

        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(30)


if __name__ == "__main__":
    main()