import numpy as np
import matplotlib.pyplot as plt

# Hypothetical dose and volume data for HPV-positive and HPV-negative tumors
dose_levels = np.arange(0, 80, 5)  # Dose levels in Gy

# Simulated volume percentages for HPV-positive tumors
hpv_positive_volumes_oropharynx = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])
hpv_positive_volumes_larynx = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])
hpv_positive_volumes_oral_cavity = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])

# Simulated volume percentages for HPV-negative tumors
hpv_negative_volumes_oropharynx = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])
hpv_negative_volumes_larynx = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])
hpv_negative_volumes_oral_cavity = np.array([100, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0])

# Plotting the DVHs
plt.figure(figsize=(8, 6))

# HPV-positive DVHs
plt.plot(dose_levels, hpv_positive_volumes_oropharynx, label='HPV+ Oropharynx', color='blue')
plt.plot(dose_levels, hpv_positive_volumes_larynx, label='HPV+ Larynx', linestyle='--', color='blue')
plt.plot(dose_levels, hpv_positive_volumes_oral_cavity, label='HPV+ Oral Cavity', linestyle=':', color='blue')

# HPV-negative DVHs
plt.plot(dose_levels, hpv_negative_volumes_oropharynx, label='HPV- Oropharynx', color='red')
plt.plot(dose_levels, hpv_negative_volumes_larynx, label='HPV- Larynx', linestyle='--', color='red')
plt.plot(dose_levels, hpv_negative_volumes_oral_cavity, label='HPV- Oral Cavity', linestyle=':', color='red')

plt.xlabel('Dose (Gy)')
plt.ylabel('Volume (%)')
plt.title('Dose Volume Histograms (DVHs) for HPV-Positive and HPV-Negative Tumors')
plt.legend()
plt.grid(True)
plt.show()
