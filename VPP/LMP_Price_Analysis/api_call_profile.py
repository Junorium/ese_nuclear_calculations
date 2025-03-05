import requests
import pandas as pd
import numpy as np
from io import BytesIO
from zipfile import ZipFile

class Node:
    def __init__(self, resource_name, df):
        self.resource_name = resource_name
        self.df = df[df['NODE'] == resource_name].copy()  # Filter data for the specific node
        self.average_price = None

    def calculate_average_price(self):
        """Calculates the average price for the node."""
        if not self.df.empty:
            self.average_price = self.df['MW'].mean()
            return self.average_price
        else:
            print(f"No data available to calculate average price for {self.resource_name}.")
            return None

# --- Main Execution Block ---
if __name__ == "__main__":
    base_url = 'http://oasis.caiso.com/oasisapi/SingleZip'
    params = {
        'queryname': 'PRC_LMP',
        'startdatetime': '20240224T00:00-0000',  #YYYYMMDD
        'enddatetime': '20250224T23:59-0000',  #YYYYMMDD
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
    else:  # The "else" statement executes if there are no exceptions
        pd.set_option('display.max_columns', None)
        print(df.head())

        # Extract unique node names
        unique_nodes = df['NODE'].unique()
        print("Unique nodes:", unique_nodes)

        # Create a Node object for each resource and perform analysis
        for resource_name in unique_nodes:
            print(f"\n--- Analyzing Node: {resource_name} ---")
            node = Node(resource_name, df)

            # Calculate and print the average price
            average_price = node.calculate_average_price()
            if average_price is not None:
                print(f"Average Price for {node.resource_name}: {average_price}")
