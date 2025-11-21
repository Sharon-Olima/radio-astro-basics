import matplotlib.pyplot as plt
import seaborn as sns  # ✅ Added for style
import pandas as pd
import numpy as np

# Set plot style using Seaborn
sns.set_style('darkgrid')  # ✅ Replaces plt.style.use('seaborn-darkgrid')

# Table 1: Spectral Wavelength Absorption Peaks
spectral_data = pd.DataFrame({
    'Drug Sample': ['Paracetamol A', 'Paracetamol B', 'Amoxicillin A', 'Amoxicillin B', 'Ciprofloxacin A', 'Ciprofloxacin B'],
    'Expected': [243, 243, 272, 272, 275, 275],
    'Measured': [244, 237, 273, 265, 275, 269]
})

# Table 2: Multi-Parameter Drug Evaluation - Final Verdict
multi_eval = pd.Series(['Authentic', 'Counterfeit', 'Authentic', 'Counterfeit', 'Authentic', 'Counterfeit']).value_counts()

# Table 3: Packaging Accuracy Test Results
packaging_verdicts = pd.Series(['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Fail']).value_counts()

# Table 4: System Performance Accuracy
performance_metrics = {
    'Spectral': 95.7,
    'Visual': 91.4,
    'Weight': 90.4,
    'Combined': 98.0
}

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Graphical Analysis of Counterfeit Drug Detection Tests', fontsize=16)

# Spectral Wavelength Bar Plot
x = np.arange(len(spectral_data['Drug Sample']))
axs[0, 0].bar(x - 0.2, spectral_data['Expected'], width=0.4, label='Expected')
axs[0, 0].bar(x + 0.2, spectral_data['Measured'], width=0.4, label='Measured')
axs[0, 0].set_title('Spectral Wavelength Absorption Peaks')
axs[0, 0].set_xticks(x)
axs[0, 0].set_xticklabels(spectral_data['Drug Sample'], rotation=45, ha='right')
axs[0, 0].set_ylabel('Wavelength (nm)')
axs[0, 0].legend()

# Multi-Parameter Drug Evaluation - Pie Chart
axs[0, 1].pie(multi_eval, labels=multi_eval.index, autopct='%1.1f%%', startangle=90, colors=['#66bb6a', '#ef5350'])
axs[0, 1].set_title('Multi-Parameter Evaluation Verdicts')

# Packaging Accuracy - Pie Chart
axs[1, 0].pie(packaging_verdicts, labels=packaging_verdicts.index, autopct='%1.1f%%', startangle=90, colors=['#42a5f5', '#ffa726'])
axs[1, 0].set_title('Packaging Accuracy Verdicts')

# System Performance Accuracy - Bar Chart
axs[1, 1].bar(performance_metrics.keys(), performance_metrics.values(), color='#ab47bc')
axs[1, 1].set_ylim(85, 100)
axs[1, 1].set_ylabel('Accuracy (%)')
axs[1, 1].set_title('System Performance Accuracy')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
