import numpy as np                  # mathematic operations and tools
import matplotlib.pyplot as plt     # visualizing plots

# Define a vector (object position)
object_position = np.array([1, 1])

# Define transformation matrices
theta = np.pi / 2                   # 'theta': a plane angle
print(theta)                        #  output: 1.5707963267948966

# Rotation matrix (90 degrees)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

# Scaling matrix (double the size)
scaling_matrix = np.array([[2, 0],
                           [0, 2]])


