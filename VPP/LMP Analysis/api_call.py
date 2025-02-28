import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from zipfile import ZipFile

base_url = 'http://oasis.caiso.com/oasisapi/SingleZip'
params = {
    'queryname': 'PRC_LMP',
    'startdatetime': '20250224T00:00-0000',
    'enddatetime': '20250224T23:59-0000',
    'version': '1',
    'market_run_id': 'DAM',  # Day-Ahead Market
    'node': 'ALL',  # Example node, you can change this
    'resultformat': '6'  # CSV format
}

response = requests.get(base_url, params=params)
if response.status_code == 200:
    with ZipFile(BytesIO(response.content)) as zf:
        csv_filename = zf.namelist()[0]
        with zf.open(csv_filename) as csv_file:
            df = pd.read_csv(csv_file)
else:
    print(f"Error: {response.status_code}")

pd.set_option('display.max_columns', None)
print(df.head())