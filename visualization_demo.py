import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Generate random points on a 3D grid
def generate_random_points(n, grid_size):
    x = np.random.uniform(0, grid_size, n)
    y = np.random.uniform(0, grid_size, n)
    z = np.random.uniform(0, grid_size, n)
    return pd.DataFrame({'x': x, 'y': y, 'z': z})

# Apply KMeans clustering
def apply_kmeans(df, k):
    kmeans = KMeans(n_clusters=k)
    df['cluster'] = kmeans.fit_predict(df[['x', 'y', 'z']])
    return df

# Plot the 3D points and color them by cluster
def plot_3d_clusters(df, k):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot with color based on the cluster
    scatter = ax.scatter(df['x'], df['y'], df['z'], c=df['cluster'], cmap='viridis', marker='o')

    ax.set_title(f'3D Clustering with K={k}')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    # Add color bar
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Cluster')

    plt.show()

# Parameters
n = 150  # Num of points
grid_size = 10  # Grid Size
k = 4  # Cluster amount

points_df = generate_random_points(n, grid_size)
clustered_df = apply_kmeans(points_df, k)
plot_3d_clusters(clustered_df, k)