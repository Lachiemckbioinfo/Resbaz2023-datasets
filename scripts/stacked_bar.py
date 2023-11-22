import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Filter the DataFrame to include only rows where Phylum is Rhodophyta
filtered_df = df[df['Phylum'] == 'Rhodophyta']

# Create a crosstab of Seqtype and Class
cross_table = pd.crosstab(filtered_df['Seqtype'], filtered_df['Class'])

# Set plot style for a clean and professional appearance
plt.style.use('seaborn-whitegrid')

# Plot the stacked bar chart with adjusted figure size
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed

# Plot with specific colors and edgecolor
colors = ['skyblue', 'orange', 'green', 'purple']
cross_table.plot(kind='bar', stacked=True, color=colors, edgecolor='black')

# Add labels and title
plt.xlabel('Seqtype', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Seqtype Counts for Phylum Rhodophyta', fontsize=14)

# Move the legend to the upper left without a legend title
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

# Save the figure in a high-resolution format (e.g., PNG)
plt.savefig('publication_figure.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
