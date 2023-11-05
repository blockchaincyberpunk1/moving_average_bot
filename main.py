# Importing the TradingBot class from the trading_bot module
from trading_bot import TradingBot

# This block of code will only be executed if this script is run as the main module
if __name__ == "__main__":
    # Creating an instance of the TradingBot class
    bot = TradingBot()
    
    # Calling the execute_trade_logic method of the TradingBot instance
    # This method contains the core functionality to make trading decisions and execute trades
    bot.execute_trade_logic()
