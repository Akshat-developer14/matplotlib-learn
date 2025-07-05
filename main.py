import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y, label='Sine Wave', color='blue', linewidth=2)

# Add title and labels
plt.title('Sine Wave using Matplotlib')
plt.xlabel('X values (radians)')
plt.ylabel('Sin(X)')

# Add a grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
