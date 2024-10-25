import numpy as np
import matplotlib.pyplot as plt

# Define a 2x2 matrix
A = np.array([[2, 1],
              [1, 2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Define the grid for the plot
xlim = [-3, 3]
ylim = [-3, 3]

# Create a grid of points
x, y = np.meshgrid(np.linspace(xlim[0], xlim[1], 20),
                   np.linspace(ylim[0], ylim[1], 20))
X = np.vstack([x.ravel(), y.ravel()])

# Apply the transformation
Y = A @ X
Y = Y.reshape(x.shape[0], x.shape[1], 2)

# Plotting
plt.figure(figsize=(10, 10))
plt.quiver(x, y, Y[..., 0] - x, Y[..., 1] - y, color='lightgray', angles='xy', scale_units='xy', scale=1)

# Plot eigenvectors
for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.T):
    plt.quiver(0, 0, eigenvector[0], eigenvector[1], color='r', angles='xy', scale_units='xy', scale=1, label=f'Eigenvector: {eigenvector}, Eigenvalue: {eigenvalue:.2f}')

# Plot the original vector space
plt.xlim(xlim)
plt.ylim(ylim)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Eigenvalues and Eigenvectors Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()