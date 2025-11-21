import numpy as np
import matplotlib.pyplot as plt

# Generate a simple sine wave
x = np.linspace(0, 10, 500)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("sin(x)")
plt.title("Simple Sine Wave Plot")
plt.grid(True)
plt.show()

