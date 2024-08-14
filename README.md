Bitcoin Price Announcer is a Python script that retrieves the current Bitcoin price from the Coindesk API and provides an audible announcement of the price. The script is designed to be cross-platform, supporting Windows, macOS, and Linux operating systems.

Features:

Fetches real-time Bitcoin price in USD using the Coindesk API.
Converts the price information into a spoken message using Google Text-to-Speech (gTTS).
Plays the audio output using platform-specific commands (start for Windows, afplay for macOS, mpg123 for Linux).
Provides a robust and straightforward way to stay updated with Bitcoin's latest value audibly.

Simply run the script to get the latest Bitcoin price and hear it announced.
The script handles errors related to API connectivity and unsupported operating systems gracefully.
This project demonstrates how to integrate APIs, handle JSON data, and use text-to-speech functionalities across different platforms.
