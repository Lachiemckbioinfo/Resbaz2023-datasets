import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming 'data.csv' contains the necessary columns
df = pd.read_csv('data.csv')

# Create a violin plot using Matplotlib and NumPy
plt.figure(figsize=(10, 6))

# Group data by 'Seqtype'
seqtypes = df['Seqtype'].unique()
seqtype_groups = [data['Orthologues'].values for _, data in df.groupby('Seqtype')]

# Create violin plot
violin_parts = plt.violinplot(seqtype_groups, showmedians=True)

# Customize the plot
plt.title('Violin Plot of Seqtype vs Orthologues')
plt.xlabel('Seqtype')
plt.ylabel('Orthologues')
plt.xticks(np.arange(1, len(seqtypes) + 1), seqtypes)

# Add annotations for each violin
for i, (seqtype, violin_part) in enumerate(zip(seqtypes, violin_parts['bodies'])):
    median = np.median(seqtype_groups[i])
    plt.text(i + 1, median, f'{seqtype}\nMedian: {median:.2f}', ha='center', va='center', fontweight='bold', color='white')

# Show the plot
plt.show()
