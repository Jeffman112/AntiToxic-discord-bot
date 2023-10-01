# AntiToxic Discord Bot

The AntiToxic Discord Bot is designed to detect toxic messages and take actions based on the toxicity score.

## Installation

Follow these steps to get the bot up and running:

1. Clone the repository:

   ```shell
   git clone https://github.com/Jeffman112/AntiToxic-discord-bot.git

2. Navigate to the project directory:

   ```shell
   cd AntiToxic-discord-bot

3. Install the required Python packages using pip:

   ```shell
   pip install -r requirements.txt

## Configuration

Before running the bot, make sure you place your bot token in the bot.py file.

## Usage
To start the bot, run the following command from the project directory:

  ```shell
  python bot.py
```

## Features
* The bot uses a pre-trained model to classify messages as toxic or safe.
* If a message is classified as toxic:
  * The bot will delete the toxic message.
  * The user who sent the toxic message will receive a 5-minute timeout.
  * The bot will send a direct message to the user explaining the action taken.

## Customization
You can customize the bot's behavior by modifying the `bot.py` script. For example, you can adjust the toxicity threshold, the timeout duration, or the bot's response.

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request.
