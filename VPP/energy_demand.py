import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('CAISO-demand-20250220.csv', index_col=0)

demand = df.iloc[2]
min_demand_time = demand.idxmin() # TIME INDEX, not min demand value
max_demand_time = demand.idxmax() # TIME INDEX, not max demand value

print(f"Minimum demand time: {min_demand_time}")
print(f"Maximum demand time: {max_demand_time}")

plt.plot(demand)

# Min, Max time indications (nodes)
plt.scatter(min_demand_time, demand.min(), color='r', zorder=5)
plt.scatter(max_demand_time, demand.max(), color='g', zorder=5)

plt.xticks(demand.index[::60])

plt.xlabel('Time (min)')
plt.ylabel('Energy demand')
plt.title("Energy Demand for 2/20/2025")

plt.show()

# daily average, over the year, for each node
# min, max price, for each node
# have this for the year