import pandas as pd

# Read the CSV file into a DataFrame
csv_file = "products1.csv"
df = pd.read_csv(csv_file)

# Process the product IDs by splitting and removing duplicates within each entry
def process_product_ids(product_ids):
    ids = product_ids.split()
    unique_ids = list(set(ids))
    return ' '.join(unique_ids)

df['productID'] = df['productID'].apply(process_product_ids)

# Remove duplicate entries based on the 'productID' column
df_unique = df.drop_duplicates(subset=['productID'])

# Write the DataFrame with unique entries to a new CSV file
output_file = "products2.csv"
df_unique.to_csv(output_file, index=False)

print("Duplicate entries removed and saved to", output_file)
