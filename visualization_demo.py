import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_random_points(n, grid_size):
    x = np.random.uniform(0, grid_size, n)
    y = np.random.uniform(0, grid_size, n)
    z = np.random.uniform(0, grid_size, n)
    return pd.DataFrame({'x': x, 'y': y, 'z': z})

def plot_3d_points(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['x'], df['y'], df['z'], c='blue', marker='o')

    ax.set_title('Random Placement of Points')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()

n = 100 # Num of points
grid_size = 10  # Grid Size

points_df = generate_random_points(n, grid_size)
plot_3d_points(points_df)

