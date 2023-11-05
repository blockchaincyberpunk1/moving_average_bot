# Moving Average Crossover Trading Bot

  [![License](https://img.shields.io/static/v1?label=License&message=MIT&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/MIT)



## Table Of Content

- [Description](#description)
- [Deployed website link](#deployedWebsite)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contribution)
- [Tests](#tests)
- [GitHub](#github)
- [Contact](#contact)
- [License](#license)




![GitHub repo size](https://img.shields.io/github/repo-size/blockchaincyberpunk1/moving_average_bot?style=plastic)

  ![GitHub top language](https://img.shields.io/github/languages/top/blockchaincyberpunk1/moving_average_bot?style=plastic)



## Description

  The Moving Average Crossover Trading Bot is a Python-based automated trading bot that executes trades based on the crossover of short-term and long-term moving averages. It utilizes Alpaca for trading and Alpha Vantage for fetching historical stock data. The bot is designed to help traders automate their trading strategies and potentially increase their trading efficiency.




<p align="center">
  <img alt="Moving Average Crossover Trading Bot" [Screenshot] src="python-trading-bot.jpg"><br>
Moving Average Crossover Trading Bot
</p>





## Installation

Follow these steps to set up and run the Moving Average Crossover Trading Bot:

Clone the Repository:

Run git clone https://github.com/blockchaincyberpunk1/moving_average_bot.git
Navigate to the project directory: cd moving_average_bot

Set Up Virtual Environment (Optional):

Run python -m venv venv
Activate the virtual environment:
On Windows: .\venv\Scripts\activate
On MacOS/Linux: source venv/bin/activate

Install Dependencies:

Run pip install -r requirements.txt

Set Up Environment Variables:

Copy the .env.example file to a new file named .env
Fill in your Alpaca and Alpha Vantage API keys in the .env file



Moving Average Crossover Trading Bot is built with the following tools and libraries: <ul><li>Pandas used for data manipulation and analysis, particularly for handling time-series data related to stock prices.</li> <li>NumPy adds support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.</li> <li>Alpaca Trade API allows the bot to interact with the Alpaca platform to fetch real-time trading data, manage accounts, and execute trades.</li> <li>Alpha Vantage API provides historical stock data that the bot uses to calculate moving averages and make trading decisions.</li></ul>





## Usage
 
To use the Moving Average Crossover Trading Bot, follow these steps:

Configure Settings:

Open config.py and adjust the settings according to your trading strategy and preferences.

Run the Bot:

Run python main.py to start the trading bot.

Monitor Trades:

The bot will print out messages to the console when it executes trades. Monitor these messages to keep track of the bot's activity.

Environment Variables

The following environment variables need to be set in your .env file:

ALPACA_API_KEY: Your Alpaca API key.
ALPACA_SECRET_KEY: Your Alpaca secret key.
ALPHA_VANTAGE_API_KEY: Your Alpha Vantage API key.





## Contribution
 
Contributions to this project are welcome! If you would like to contribute, feel free to open issues, submit pull requests, or make suggestions for improvements.





## Tests
 
To test the Moving Average Crossover Trading Bot, you can:

Run the Bot in Paper Trading Mode:

Ensure that you are using Alpaca's paper trading API endpoint in config.py.
Run the bot and monitor the trades it executes in the paper trading environment.







## GitHub

<a href="https://github.com/blockchaincyberpunk1"><strong>blockchaincyberpunk1</a></strong>



<p>Visit my website: <strong><a href="http://blockchaincyberpunk1.github.io/thepolyglot">The Polyglot</a></strong></p>





## Contact

Feel free to reach out to me on my email:
thepolyglot8@gmail.com





## License

[![License](https://img.shields.io/static/v1?label=Licence&message=MIT&color=blue)](https://opensource.org/license/MIT)


