import numpy as np                  # mathematic operations and tools
import matplotlib.pyplot as plt     # visualizing plots

# Define a vector (object position)
object_position = np.array([1, 1])

# Define transformation matrices
theta = np.pi / 2                   # 'theta': a plane angle

# Rotation matrix (90 degrees)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

# Scaling matrix (double the size)
scaling_matrix = np.array([[2, 0],
                           [0, 2]])

# Combine transformations (rotate then scale)
# @ calculates the product of two matrices
portal_transform = scaling_matrix @ rotation_matrix

# Apply the portal transformation
transformed_position = portal_transform @ object_position

print(transformed_position)         # output: [-2.  2.]
