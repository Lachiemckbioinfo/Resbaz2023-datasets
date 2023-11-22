import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Filter the DataFrame to include only rows where Phylum is Rhodophyta
filtered_df = df[df['Phylum'] == 'Rhodophyta']

# Plot the bar chart
filtered_df['Class'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Bar Chart of Class Counts for Phylum Rhodophyta')

# Show the plot
plt.show()
