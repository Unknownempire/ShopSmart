import pandas as pd

# Load the data with custom separator and handle missing values
# Function to get recommendations

class user_similarity :
    def get_Recommendation(self,customer_id) :
        data = pd.read_csv('./collaborative_model/products2.csv', sep=',', na_values=['', ' ', 'nan', 'NAN'])

# Drop rows with missing 'uid' or 'productID' values
        data = data.dropna(subset=['uid', 'productID'])

# Convert 'productID' column to a list of strings
# data['productID'] = data['productID'].apply(lambda x: [item.strip() for item in x.split("-") if item.strip()])
        data['productID'] = data['productID'].apply(lambda x: [f'{item.strip()}' for item in x.split(" ") if item.strip()])

# Create a list of unique product names
        all_products = set(item for sublist in data['productID'] for item in sublist)

# Create a pivot table with product names as columns
        pivot_table = pd.DataFrame(columns=all_products, index=data['uid'])
        for idx, row in data.iterrows():
            products = row['productID']
            pivot_table.loc[row['uid'], products] = 1

        pivot_table.fillna(0, inplace=True)
# Calculate the correlation between items
        correlation = pivot_table.corr()
# print(correlation)
    # def get_recommendations(customer_id):
        customer_purchases = pivot_table.loc[customer_id]

    # Calculate the similarity scores
        similar_items = correlation.dot(customer_purchases)
    # print(similar_items)
    
    # Filter out already purchased items
        columnID = ['value']
    # similar_items = similar_items[similar_items.index.isin(customer_purchases.index) == False]
        df = pd.DataFrame(similar_items, columns=columnID)
    # print(df)
        recommendations = df[df['value'] <= 1]
    # print(recommendations)
    # print(similar_items) 
    # Get the recommended items
        recommended_items = recommendations.sort_values(by='value', ascending=False)
        # ans = recommended_items.drop(columns=['value'])
        ans = recommended_items.index[0:5].tolist()

        #changing list of strings to list of integer
        for i in range(0, len(ans)):
            ans[i] = int(ans[i])
 

        product_csv=pd.read_csv('products.csv')
        # filtered_data = product_csv[product_csv['pid'].astype(str).isin(ans)]
        filtered_data = product_csv.loc[product_csv['pid'].isin(ans)].values.tolist()

        # selected_columns = ['product_name', 'price', 'brand']
        # filtered_data = filtered_data[selected_columns]

        # print(ans)
        # print("--------Filter Data------")
        # filtered_data.reset_index(drop=True, inplace=True)  # Reset the index

        # print(filtered_data.to_string(index=False))  # Setting index=False to not display the index
        print('filtered_data = ',filtered_data)
        # print(product_csv)
        print(ans)
        # return(filtered_data.to_string(index=False))
        return filtered_data
        # return ans



# User_Simi = user_similarity()
# User_Simi.get_Recommendation(46)
