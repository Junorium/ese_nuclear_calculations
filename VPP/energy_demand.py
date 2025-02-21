import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('CAISO_demand.csv', header=None)
print(df.head)
print("-----")
print(df.columns)