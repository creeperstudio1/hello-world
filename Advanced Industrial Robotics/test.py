import matplotlib.pyplot as plt
import numpy as np

# Sample data
theta_values = np.linspace(0, 2 * np.pi, 360)  # Values for theta in radians
r_values = np.sin(2 * theta_values)  # Example radial values (replace with your data)

# Create a polar plot
plt.figure(figsize=(8, 8))
plt.polar(theta_values, r_values, label='Example Curve', color='blue')

# Customize the plot
plt.title('Polar Plot with Theta Values')
plt.legend()

# Show the plot
plt.show()