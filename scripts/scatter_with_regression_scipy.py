import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

# Load the data from Excel file
df = pd.read_csv('data.csv')

# Define colors for each column
column_colors = {'Compounds_modules': '#1f78b4',  # Blue
                  'Compounds_reactions': '#33a02c'}  # Green

# Define shapes for each column
shapes = {'Compounds_modules': 'o',  # Circle
          'Compounds_reactions': 'o'}  # Square

# Create a scatter plot with regression lines and R-squared values
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

for column, shape in shapes.items():
    sns.regplot(x='Orthologues',
                y=column,
                data=df,
                scatter_kws={'color': column_colors[column], 'marker': shape},
                line_kws={'color': column_colors[column], 'linewidth': 2},
                label=f'{column}')

    # Calculate R-squared value
    slope, intercept, r_value, p_value, std_err = linregress(df['Orthologues'], df[column])
    r_squared = r_value**2

    # Annotate the plot with R-squared values
    y_position = 0.1 if column == 'Compounds_reactions' else 0.02
    plt.annotate(f'R-squared: {r_squared:.3f}', xy=(0.95, y_position),
                 xycoords='axes fraction', ha='right', color=column_colors[column])

# Set labels and title
plt.xlabel('Orthologues')
plt.ylabel('Count')
plt.title('Linear Regression Analysis for Compounds and Orthologues')

# Create a legend for shapes with colored markers
shape_legend_labels = [plt.Line2D([0], [0], marker=shape, color='w', label=f'{column}', markerfacecolor=column_colors[column], markersize=10)
                       for column, shape in shapes.items()]

plt.legend(handles=shape_legend_labels, title='Column', loc='upper right')

# Save the figure as an SVG file
plt.savefig('linear_regression_analysis_with_r_squared_adjusted_position.svg', format='svg', bbox_inches='tight')

# Show the plot
plt.show()

