# Discord Bot for Monitoring H1Emu Server Status
This Discord bot is designed to monitor the status of the H1Emu server and display the number of players online as the bot's status. The bot uses the discord.py library to interact with Discord and the requests and beautifulsoup4 libraries to scrape the H1Emu server website for the player count.

**Dependencies**
To run this script on Linux, you will need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

In addition to Python 3, you will also need to install the following dependencies:

* discord.py
* requests
* beautifulsoup4
You can install these dependencies using pip:

Copy code
```pip3 install discord.py requests beautifulsoup4```

**Usage**
To start the bot run the following command in your terminal:

Copy code
```python3 main.py```

The bot will continuously check the status of the H1Emu server and update its presence on Discord with the number of players online. If you want to change the server being monitored, you can edit the script and replace the URL with the URL of the server you want to monitor.
