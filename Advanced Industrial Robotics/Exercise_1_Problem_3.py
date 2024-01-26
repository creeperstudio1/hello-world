import matplotlib.pyplot as plt
import numpy as np

# Plotting points
x_points = [0, 1, 2, 3, 0]
y_points = [0, 0, 0, 0, 1]

# Plotting curves (Hough transform) in the first figure
plt.figure()
theta_values = np.linspace(0, np.pi, 100)

for i in range(5):
    rho_values = x_points[i] * np.cos(theta_values) + y_points[i] * np.sin(theta_values)
    plot_label = "Curve" + str(i + 1)
    plt.plot(theta_values, rho_values, label=plot_label)

# Customize the first plot
plt.scatter(0.5 * np.pi, 0, color='red', label='theta=pi/2')
plt.title('Hough transform')
plt.xlabel('Theta-axis')
plt.ylabel('Rho-axis')
plt.legend()
plt.grid(True)

# Show the first figure
plt.show()

# Plotting points in the second figure
plt.scatter(x_points, y_points, color='blue', label='Data points')

# Plotting the line y=0 in the second figure
plt.axhline(y=0, color='red', linestyle='--', label='y=0')

# Customize the second plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Points and Line Plot')
plt.legend()
plt.grid(True)

# Show the second figure
plt.show()