import numpy as np
import matplotlib.pyplot as plt

# Define vertices of a square
square = np.array([[1, 1],
                   [1, -1],
                   [-1, -1],
                   [-1, 1]])

# Add the first point again to close the shape
square = np.vstack([square, square[0]])

# Transformation matrices
theta = np.pi / 4  # 45 degrees rotation
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

scaling_matrix = np.array([[3, 0],
                           [0, 3]])

shear_matrix = np.array([[1, 1.5],
                         [0, 1]])

reflection_matrix = np.array([[-1, 0],
                              [0, 1]])

# Combine all transformations
portal_transform = rotation_matrix @ scaling_matrix @ shear_matrix @ reflection_matrix

# Apply transformation to each point of the square
transformed_square = np.apply_along_axis(lambda point: portal_transform @ point, 1, square)

# Plot the results
plt.figure(figsize=(10, 10))
plt.plot(square[:, 0], square[:, 1], 'b-', label='Original Square')
plt.plot(transformed_square[:, 0], transformed_square[:, 1], 'r-', label='Transformed Square')

# Plot arrows for the first point to highlight transformation
plt.quiver(square[0, 0], square[0, 1], transformed_square[0, 0] - square[0, 0], transformed_square[0, 1] - square[0, 1], 
           color='g', scale=1, scale_units='xy', angles='xy', label='Transformation Path')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend()
plt.title("Interdimensional Square Transformation")
plt.show()