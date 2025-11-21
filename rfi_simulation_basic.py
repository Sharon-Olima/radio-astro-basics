import numpy as np
import matplotlib.pyplot as plt

# Create a simple signal
x = np.linspace(0, 1, 2000)
signal = np.sin(40 * np.pi * x)  # base signal

# Add a simulated narrow RFI spike
signal[900:920] += 5  # RFI-like jump

plt.plot(x, signal)
plt.title("Simulated Signal with Simple RFI Spike")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

