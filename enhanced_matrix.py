import numpy as np
import matplotlib.pyplot as plt

# Define an object position
object_position = np.array([1, 1])

# Transform matrices (enhanced for shear and reflection)
# Rotation (45 degrees)
theta = np.pi / 4
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

# Scaling (triple the size)
scaling_matrix = np.array([[3, 0], 
                           [0, 3]])

# Shear (slide it)
shear_matrix = np.array([[1, 1.5],  # Shear in x-direction
                         [0, 1]])

# Reflection (flip over y-axis)
reflection_matrix = np.array([[-1, 0],
                              [0, 1]])

# Combine all transformations
# Order matters here: Reflection, Shear, Scale, then Rotate
portal_transform = rotation_matrix @ scaling_matrix @ shear_matrix @ reflection_matrix

# Apply the portal transformation
transformed_position = portal_transform @ object_position

# Plot the results
plt.figure()
plt.quiver(0, 0, object_position[0], object_position[1], color='b', label='Original Position')
plt.quiver(0, 0, transformed_position[0], transformed_position[1], color='r', label='Transformed Position')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.grid()
plt.legend()
plt.title("Enhanced Interdimensional Portal Simulation")
plt.show()

print("Original Position, Morty:", object_position)
print("Transformed Position, Morty:", transformed_position)