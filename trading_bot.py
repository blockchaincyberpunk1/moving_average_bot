# Importing necessary libraries
import alpaca_trade_api as tradeapi  # Used for interacting with the Alpaca trading API
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL, SHORT_TERM_WINDOW, LONG_TERM_WINDOW, SYMBOL  # Importing configuration settings
from data_provider import DataProvider  # Importing the DataProvider class to fetch historical stock data
import pandas as pd  # Used for data manipulation and analysis

# Defining a class named TradingBot
class TradingBot:
    # Constructor method to initialize the TradingBot object
    def __init__(self):
        # Setting up the Alpaca API connection
        self.api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)
        # Creating an instance of DataProvider to fetch historical stock data
        self.data_provider = DataProvider()

    # Method to calculate short-term and long-term moving averages
    def calculate_moving_averages(self, df):
        # Calculating the short-term moving average and adding it as a new column to the DataFrame
        df["short_mavg"] = df["close"].rolling(window=SHORT_TERM_WINDOW, min_periods=1).mean()
        # Calculating the long-term moving average and adding it as a new column to the DataFrame
        df["long_mavg"] = df["close"].rolling(window=LONG_TERM_WINDOW, min_periods=1).mean()
        # Returning the DataFrame with the new moving average columns
        return df

    # Method to execute the trading logic based on moving average crossovers
    def execute_trade_logic(self):
        # Fetching historical stock data
        df = self.data_provider.get_historical_data()
        # Calculating moving averages
        df = self.calculate_moving_averages(df)
        # Checking for a crossover to execute a buy order
        if df["short_mavg"].iloc[-1] > df["long_mavg"].iloc[-1] and df["short_mavg"].iloc[-2] <= df["long_mavg"].iloc[-2]:
            # Submitting a buy order to Alpaca
            self.api.submit_order(
                symbol=SYMBOL,
                qty=1,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            # Printing a confirmation message to the console
            print("Buy Order Executed")
        # Checking for a crossover to execute a sell order
        elif df["short_mavg"].iloc[-1] < df["long_mavg"].iloc[-1] and df["short_mavg"].iloc[-2] >= df["long_mavg"].iloc[-2]:
            # Submitting a sell order to Alpaca
            self.api.submit_order(
                symbol=SYMBOL,
                qty=1,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            # Printing a confirmation message to the console
            print("Sell Order Executed")
