import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from zipfile import ZipFile
from datetime import datetime, timedelta

class Node:
    def __init__(self, resource_name, df):
        self.resource_name = resource_name
        self.df = df[df['NODE'] == resource_name].copy()  # Filter data for the specific node and create a copy

        # Convert 'INTERVALSTARTTIME_GMT' to datetime objects during Node initialization
        try:
            self.df.loc[:, 'INTERVALSTARTTIME_GMT'] = pd.to_datetime(self.df['INTERVALSTARTTIME_GMT'])
        except Exception as e:
            print(f"Error converting 'INTERVALSTARTTIME_GMT' to datetime for {self.resource_name}: {e}")
            self.df['INTERVALSTARTTIME_GMT'] = None  #Or you can set to NaT

        self.yearly_average_price = None

    def calculate_yearly_average_price(self):
        """Calculates the average price point over the entire year."""
        if not self.df.empty:
            self.yearly_average_price = self.df['MW'].mean()  # Use 'MW' directly from the DataFrame
            return self.yearly_average_price
        else:
            print(f"No data available to calculate yearly average for {self.resource_name}.")
            return None

    def plot_yearly_average_price(self):
        """Plots the average price over the year (each data point)."""
        if self.df.empty or self.df['INTERVALSTARTTIME_GMT'].isnull().all(): #Check if there is any data or if the datetimes are invalid
            print(f"No valid data available to plot yearly average for {self.resource_name}.")
            return

        # Group by date and calculate the daily average price
        daily_average = self.df.groupby(self.df['INTERVALSTARTTIME_GMT'].dt.date)['MW'].mean()

        # Convert index to datetime objects and sort
        daily_average.index = pd.to_datetime(daily_average.index)
        daily_average = daily_average.sort_index()

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(daily_average.index, daily_average.values, marker='o', linestyle='-')
        plt.xlabel("Date")
        plt.ylabel("Average Daily Price")
        plt.title(f"Yearly Average Price for {self.resource_name}")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_daily_price_trend(self):
        """Plots the daily price trend (each time interval averaged over the year)."""
        average_prices = self.calculate_daily_price_trend()
        if average_prices is None or average_prices.empty:
            print(f"No data available to plot daily price trend for {self.resource_name}.")
            return

        # Convert time objects to strings for plotting
        time_labels = [time.strftime('%H:%M') for time in average_prices.index]

        plt.figure(figsize=(12, 6))
        plt.plot(time_labels, average_prices.values, marker='o', linestyle='-')
        plt.xlabel("Time of Day (GMT)")
        plt.ylabel("Average Price")
        plt.title(f"Daily Price Trend for {self.resource_name}")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def calculate_daily_price_trend(self):
        """Calculates the average price for each time interval over the year."""
        if self.df.empty or self.df['INTERVALSTARTTIME_GMT'].isnull().all():
            print(f"No data available to calculate daily price trend for {self.resource_name}.")
            return None

        # Group data by time and calculate average price
        self.df['TIME'] = self.df['INTERVALSTARTTIME_GMT'].dt.time
        average_prices = self.df.groupby('TIME')['MW'].mean()
        return average_prices

# --- Main Execution Block ---
if __name__ == "__main__":
    base_url = 'http://oasis.caiso.com/oasisapi/SingleZip'
    params = {
        'queryname': 'PRC_LMP',
        'startdatetime': '20250224T00:00-0000', #YYYYMMDD
        'enddatetime': '20250224T23:59-0000', #YYYYMMDD
        'version': '1',
        'market_run_id': 'DAM',  # Day-Ahead Market
        'node': 'ALL',  # Fetch data for all nodes
        'resultformat': '6'  # CSV format
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with ZipFile(BytesIO(response.content)) as zf:
            csv_filename = zf.namelist()[0]
            with zf.open(csv_filename) as csv_file:
                df = pd.read_csv(csv_file)
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")
    else: #The "else" statement executes if there are no exceptions
        pd.set_option('display.max_columns', None)
        print(df.head())

        # Extract unique node names
        unique_nodes = df['NODE'].unique()
        print("Unique nodes:", unique_nodes)

        # Create a Node object for each resource and perform analysis
        for resource_name in unique_nodes:
            print(f"\n--- Analyzing Node: {resource_name} ---")
            node = Node(resource_name, df)

            # Calculate and print the yearly average price
            yearly_average = node.calculate_yearly_average_price()
            if yearly_average is not None:
                print(f"Yearly Average Price for {node.resource_name}: {yearly_average}")

            # Plot the yearly average price
            node.plot_yearly_average_price()

            # Plot the daily price trend
            node.plot_daily_price_trend()
