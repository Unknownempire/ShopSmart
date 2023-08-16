import pandas as pd

# Load the data
data = pd.read_csv('products2.csv', sep=',', na_values=['', ' ', 'nan', 'NAN'])

# Drop rows with missing 'uid' or 'productID' values
data = data.dropna(subset=['uid', 'productID'])

# Create a pivot table
pivot_table = data.pivot_table(index='uid', columns='productID', aggfunc='size', fill_value=0)

# Calculate the correlation between items
correlation = pivot_table.corr()

# Get customer's purchased items
customer_id = 46
customer_purchases = pivot_table.loc[customer_id]

# Calculate the similarity scores with other items
similar_items = correlation.dot(customer_purchases)

# Filter out items that have already been purchased
recommended_items = similar_items[similar_items.index.isin(customer_purchases.index) == False]

# Get the top N recommended items
top_recommended_items = recommended_items.nlargest(5)

print("Top 5 Recommended Product IDs:")
print(top_recommended_items.index.tolist())
