import pandas as pd

# Read the three CSV files
results_1 = pd.read_csv('results_1.csv')
results_2 = pd.read_csv('results_2.csv')
results_3 = pd.read_csv('results_3.csv')

# Merge the dataframes
merged_df = pd.concat([results_1, results_2, results_3], axis=0, ignore_index=True)

# Fill in missing values with non-null values from other columns
merged_df = merged_df.groupby(merged_df.columns, axis=1).apply(lambda x: x.ffill().bfill())

# Write the merged dataframe to a new CSV file
merged_df.to_csv('merged_results.csv', index=False)
