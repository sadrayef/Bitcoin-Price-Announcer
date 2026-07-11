# ₿ Bitcoin Price Announcer

A lightweight cross-platform Python application that retrieves the latest Bitcoin price from the CoinGecko API and announces it using Google Text-to-Speech (gTTS).

The application continuously monitors the Bitcoin price, announces it aloud every five minutes, and runs until manually stopped.

---

## Features

- 📈 Fetches the latest Bitcoin price in USD
- 🔊 Announces the price using text-to-speech
- 🔄 Automatically updates every 5 minutes
- 🌍 Cross-platform support
  - Windows
  - macOS
  - Linux
- ⚠️ Graceful network error handling
- 🛑 Stops safely with `Ctrl + C`

---

## Demo

![Terminal Demo](demo.png)

---

## Requirements

- Python 3.9+
- Internet connection

Required packages:

```bash
pip install -r requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Bitcoin-Price-Announcer.git
```

Navigate into the project:

```bash
cd Bitcoin-Price-Announcer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python btc_price.py
```

Example output:

```text
Bitcoin Price Announcer started.
Press Ctrl+C to stop.

Bitcoin's current price is 64,267.00 USD
Next announcement in 5 minutes.
```

Terminate the application at any time using:

```text
Ctrl + C
```

---

## Technologies Used

- Python
- Requests
- Google Text-to-Speech (gTTS)
- CoinGecko API

---

## Project Structure

```
Bitcoin-Price-Announcer
│
├── btc_price.py
├── requirements.txt
├── README.md
├── assets/
│   └── demo.png
└── .gitignore
```

---

## Future Improvements

- Support multiple cryptocurrencies
- User-configurable update interval
- Desktop notifications
- Price change alerts
- Support for multiple currencies (EUR, GBP, etc.)

---

## License

This project is licensed under the MIT License.

---

## Author

Sadra
