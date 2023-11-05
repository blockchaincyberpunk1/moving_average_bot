# Importing necessary libraries
import requests  # Used for making HTTP requests to the Alpha Vantage API
import pandas as pd  # Used for data manipulation and analysis
from config import ALPHA_VANTAGE_BASE_URL, ALPHA_VANTAGE_API_KEY, SYMBOL  # Importing configuration settings

# Defining a class named DataProvider
class DataProvider:
    # Defining a method to fetch historical stock data
    def get_historical_data(self):
        # Setting up the parameters for the API request
        params = {
            "function": "TIME_SERIES_DAILY",  # Fetching daily time series data
            "symbol": SYMBOL,  # Stock symbol for which the data is to be fetched
            "apikey": ALPHA_VANTAGE_API_KEY,  # API key for authentication
            "outputsize": "compact",  # Fetching only the latest 100 data points
            "datatype": "json"  # Specifying the format of the response
        }
        
        # Making an HTTP GET request to the Alpha Vantage API
        response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
        
        # Parsing the JSON response to extract the time series data
        data = response.json()["Time Series (Daily)"]
        
        # Converting the dictionary to a Pandas DataFrame for easier manipulation
        df = pd.DataFrame.from_dict(data, orient="index").sort_index()
        
        # Returning the DataFrame with all values converted to float for numerical calculations
        return df.astype(float)
