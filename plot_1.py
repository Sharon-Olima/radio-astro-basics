import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample data
data = {
    'Tumor Site': ['Oropharynx', 'Larynx', 'Oral Cavity'],
    'HPV-16': [48, 38, 35],
    'HPV-18': [12, 16, 25],
    'HPV-45': [8, 8, 5],
    'HPV Negative': [32, 38, 35]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))

# Stacked bar chart
df.set_index('Tumor Site').T.plot(kind='bar', stacked=True, ax=ax, color=['blue', 'orange', 'green', 'red'])

# Labels and title
ax.set_ylabel('Percentage of Patients (%)')
ax.set_title('HPV Genotype Prevalence and Distribution Across Tumor Sites')
plt.xticks(rotation=0)
plt.legend(title="HPV Genotype")
plt.show()
