import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Filter the DataFrame for rows where the Phylum is 'Rhodophyta'
df_rhodophyta = df[df['Phylum'] == 'Rhodophyta']

# Create a DataFrame with the count of items for each combination of 'Seqtype' and 'Class'
df_counts = df_rhodophyta.groupby(['Seqtype', 'Class']).size().unstack()

# Set a color palette for better visualization
colors = sns.color_palette("Set3")

# Create a larger figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# Create a stacked barplot using Seaborn
df_counts.plot(kind='bar', stacked=True, color=colors, ax=ax, edgecolor='black', linewidth=0.5)
plt.title('Stacked Barplot of Total Items for Each Class (Colored by Seqtype)\n(Phylum: Rhodophyta)')
plt.xlabel('Class')
plt.ylabel('Total Items')

# Move the legend to the side
plt.legend(title='Seqtype', bbox_to_anchor=(1, 1), loc='upper left')

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the y-axis label to better fit the plot
plt.subplots_adjust(right=0.85)

# Save the plot as an image (optional)
# plt.savefig('stacked_barplot_class_seqtype_rhodophyta.png', dpi=300, bbox_inches='tight')

plt.show()
