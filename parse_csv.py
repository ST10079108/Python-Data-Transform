import csv
import pandas as pd

#with open('raw_data.csv', 'r') as csv_file:
#    csv_reader = csv.reader(csv_file)

#    with open('new_data.csv', 'w') as new_file:
 #       csv_writer = csv.writer(new_file, delimiter='-')
#
 #       for line in csv_reader:
  #          csv_writer.writerow(line)


# Raw data file loaded

df = pd.read_csv("raw_data.csv")

# Data validation

print(f"Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print("\nFirst few lines of data:")
print(df.head())

# Transformation, adjust column names and rows with null values are removed

df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.dropna()

# Save cleaned data

df.to_csv("cleaned_data.csv", index=False)

