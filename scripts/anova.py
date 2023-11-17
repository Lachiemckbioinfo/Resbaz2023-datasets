import pandas as pd
from scipy.stats import f_oneway

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Filter the DataFrame for rows where the Phylum is 'Rhodophyta'
df_rhodophyta = df[df['Phylum'] == 'Rhodophyta']

# Perform ANOVA for the number of proteins across different classes
classes = df_rhodophyta['Class'].unique()
anova_results = {}

for cls in classes:
    data = df_rhodophyta[df_rhodophyta['Class'] == cls]['Proteins']
    anova_results[cls] = data

# Perform the ANOVA test
f_statistic, p_value = f_oneway(*anova_results.values())

# Output the results
print("ANOVA Results:")
print(f"F-Statistic: {f_statistic}")
print(f"P-Value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("The p-value is less than 0.05, so we reject the null hypothesis.")
    print("There is a significant difference in the number of proteins among different classes.")
else:
    print("The p-value is greater than or equal to 0.05.")
    print("There is no significant difference in the number of proteins among different classes.")
