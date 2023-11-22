import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming 'data.csv' contains the necessary columns
df = pd.read_csv('data.csv')

# Extract the columns of interest
proteins = df['Proteins']
compounds = df['Compounds']

# Create a scatter plot
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
plt.scatter(proteins, compounds, color='blue', alpha=0.7, edgecolors='black')

# Add labels and title
plt.xlabel('Proteins')
plt.ylabel('Compounds')
plt.title('Scatter Plot of Proteins vs Compounds')

# Perform linear regression using numpy
coefficients = np.polyfit(proteins, compounds, 1)
line = np.polyval(coefficients, proteins)
plt.plot(proteins, line, color='red', label=f'Linear Regression\nR-squared: {np.corrcoef(proteins, compounds)[0, 1]**2:.3f}')

# Add legend
plt.legend()

# Show the plot
plt.show()
