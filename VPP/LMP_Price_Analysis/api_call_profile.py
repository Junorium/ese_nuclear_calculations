import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from zipfile import ZipFile
from datetime import datetime, timedelta

class Node:
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.daily_data = {}  # Store daily dataframes
        self.yearly_average_price = None

    def fetch_caiso_data(self, start_date, end_date):
        """Fetches CAISO price data for the specified date range."""
        base_url = 'http://oasis.caiso.com/oasisapi/SingleZip'
        date_range = pd.date_range(start=start_date, end=end_date)

        for date in date_range:
            date_str = date.strftime('%Y%m%d')
            params = {
                'queryname': 'PRC_LMP',
                'startdatetime': f'{date_str}T00:00-0000',
                'enddatetime': f'{date_str}T23:59-0000',
                'version': '1',
                'market_run_id': 'DAM',  # Day-Ahead Market
                'node': self.resource_name,
                'resultformat': '6'  # CSV format
            }

            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                with ZipFile(BytesIO(response.content)) as zf:
                    try:
                        csv_filename = zf.namelist()[0]
                        with zf.open(csv_filename) as csv_file:
                            df = pd.read_csv(csv_file)
                            # Convert Trading Interval to Datetime
                            df['INTERVALSTARTTIME_GMT'] = pd.to_datetime(df['INTERVALSTARTTIME_GMT'])
                            df = df.rename(columns={'MW': 'PRICE'})
                            self.daily_data[date] = df
                    except Exception as e:
                        print(f"Error processing CSV for {date}: {e}")

            else:
                print(f"Error: {response.status_code} for {date}")

    def calculate_yearly_average_price(self):
        """Calculates the average price point over the entire year."""
        all_prices = []
        for date, df in self.daily_data.items():
            all_prices.extend(df['PRICE'].tolist())

        if all_prices:
            self.yearly_average_price = np.mean(all_prices)
        else:
            self.yearly_average_price = None
        return self.yearly_average_price

    def plot_yearly_average_price(self):
        """Plots the average price over the year (365 points)."""
        if not self.daily_data:
            print("No data available to plot yearly average.")
            return

        # Combine all daily dataframes into one
        yearly_df = pd.concat(self.daily_data.values(), ignore_index=True)
        # Group by date and calculate the daily average price
        daily_average = yearly_df.groupby(yearly_df['INTERVALSTARTTIME_GMT'].dt.date)['PRICE'].mean()

        # Convert index to datetime objects
        daily_average.index = pd.to_datetime(daily_average.index)

        # Sort the index
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

    def calculate_daily_price_trend(self):
        """Calculates the average price for each time interval over the year."""
        # Aggregate data for each timestamp across all days
        all_data = []
        for df in self.daily_data.values():
            all_data.append(df)

        combined_df = pd.concat(all_data, ignore_index=True)
        # Group data by time and calculate average price
        combined_df['TIME'] = combined_df['INTERVALSTARTTIME_GMT'].dt.time
        average_prices = combined_df.groupby('TIME')['PRICE'].mean()
        return average_prices

    def plot_daily_price_trend(self):
        """Plots the daily price trend (each time interval averaged over the year)."""
        average_prices = self.calculate_daily_price_trend()
        if average_prices is None or average_prices.empty:
            print("No data available to plot daily price trend.")
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

# --- Example Usage ---
if __name__ == "__main__":
    #Specify the Resource Name:
    resource_name = 'PALOVRDE_1_N001'  # You can change this

    #Specify the start and end date
    start_date = '2024-01-01' #YYYY-MM-DD
    end_date = '2024-01-05' #YYYY-MM-DD
    #end_date = '2024-12-31'  # One year of data, for demonstration purposes, you can fetch over the year

    # Create a Node object
    node = Node(resource_name)
    # Fetch data
    node.fetch_caiso_data(start_date, end_date)

    # Check that data was actually loaded
    if node.daily_data:
        # Calculate and print the yearly average price
        yearly_average = node.calculate_yearly_average_price()
        print(f"Yearly Average Price for {node.resource_name}: {yearly_average}")

        # Plot the yearly average price
        node.plot_yearly_average_price()

        # Plot the daily price trend
        node.plot_daily_price_trend()
    else:
        print(f"No data was found for the specified time interval, {start_date} to {end_date}")