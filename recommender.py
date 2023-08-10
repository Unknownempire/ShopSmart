import random
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity 
from fuzzywuzzy import fuzz
import time
import datetime

class Recommend :
    def __init__(self):
        self.orderDetails = self.get_order_details()
        self.browserHistory = self.get_browser_history()
        self.products,self.productList,self.numOfProducts = self.get_products()
        self.correlationData = self.get_correlation_data()

    # Load orderHistory from CSV file
    def get_order_details(self):
       orderDetails = pd.read_csv('orderHistory.csv')
       return orderDetails
    
    # Load browserHistory from CSV file
    def get_browser_history(self):
        browserHistory = pd.read_csv("browseHistory.csv")
        return browserHistory
    
    # Load product_details from CSV file
    def get_products(self):
        products = pd.read_csv('products.csv')
        productList = products.values.tolist()
        numOfProducts = len(productList)
        return products, productList, numOfProducts
    
    # Load correlation_data from CSV file

    def get_correlation_data(self):
        correlationData = pd.read_csv('correlationData.csv')
        return correlationData
    
    # Now we will give recommendation based on
    # the user's previous orders and their browsing history
    # we will calculate the latest purchase and the brand purchased by the user

    #Later [
    # then find out which other brands are similar to it in terms of price and rating -- we can add
    # more features like number of ratings or reviews etc later]


    # Calculate weights for the "date" attribute, which gives higher weight to products ordered RECENTLY by the specific user.
    def calculate_date_weights(self,user_id):
        order_history = self.orderDetails.loc[self.orderDetails['uid'] == user_id]
        date_data = np.zeros(self.numOfProducts)
        max_date = 0
        min_date = 100000000000

        for index,order in order_history.iterrows():
            current_pid = order['pid']
            order_date = order['date']
            order_time_stamp = time.mktime(datetime.datetime.strptime(order_date,'%d/%m/%Y').timetuple())
            max_date = max(max_date,order_time_stamp)
            min_date = min(min_date,order_time_stamp)
        
        for index,order in order_history.iterrows():
            current_pid = order['pid']
            order_date = order['date']
            order_time_stamp = time.mktime(datetime.datetime.strptime(order_date,'%d/%m/%Y').timetuple())
            date_difference = max_date - min_date
            normalized_date = 0.15 if float(order_time_stamp - min_date) / (date_difference + 1e-6) == 0 else float((order_time_stamp-min_date)/(date_difference + 1e-6))   # Adding epsilon
            date_data[current_pid] = normalized_date
        return date_data

    def calculate_brand_weights(self,user_id):
        order_history = self.orderDetails.loc[self.orderDetails['uid'] == user_id]
        print(order_history)
        user_brand_data = np.zeros(self.numOfProducts)
        visited = set()
        pid_bought = order_history['pid'].values.tolist()

        for pid in pid_bought:
            brand = self.products['brand'].values.tolist()[pid]
            if brand not in visited:
                visited.add(brand)
                count = 0
                for product in self.productList:
                    if product[3] == brand:
                        user_brand_data[count] = 1
                    count = count+1
        return user_brand_data
    
    #Testing recommendation of single product ----> need to call correlation matrix before calling this function
    def calculate_single_product_recommendation(self,product_id):
        product_corr = self.correlation_matrix[product_id]
        recommend_product = []
        for i in range (0,len(product_corr)):
            recommend_product.append([product_corr[i],i])
        recommend_product = sorted(recommend_product,reverse=True)

        for i in range (0,10):
            print(product_corr[recommend_product[i][1]],self.productList[recommend_product[i][1]])
        return recommend_product

# #     #recommender_instance = Recommender()

# #  Define the product ID for which you want to get recommendations
# # product_id = 1  # Replace with the desired product ID

# #  Call the getCorrelationMatrix function to compute the correlation matrix
# # correlation_matrix = recommender_instance.getCorrelationMatrix(46)  # Replace user_id with the appropriate user ID

# #  Set the correlationMatrix attribute in the instance
# # recommender_instance.correlationMatrix = correlation_matrix

# #  Call the getSingleProductRecommendation function on the instance
# # recommender_instance.getSingleProductRecommendation(1)
    def calculate_correlation_matrix(self,user_id):
        price_data = self.correlationData['price'].values.tolist()
        date_data = self.calculate_date_weights(user_id)
        name_data = self.correlationData['name'].values.tolist()
        brand_data = self.correlationData['brand'].values.tolist()
        user_brand_data = self.calculate_brand_weights(user_id)

        totalData=[price_data,date_data,name_data,brand_data,user_brand_data]
        index=['price','date','name','brand','userBrandPreference']
        
        productXAttributes = pd.DataFrame(data=totalData,index=index,columns=self.products['product_name'].values.tolist())

        productXAttributes = productXAttributes.T
        productXAttributes = productXAttributes.astype(float)
        productXAttributes = productXAttributes.dropna()
        productXAttributes.to_csv("TemporaryMatrix.csv",index=False)
        print(productXAttributes)
        print(np.corrcoef(productXAttributes))

        corrcoef = np.corrcoef(productXAttributes)
        return corrcoef

    def calculate_product_Recommendation(self,user_id):
        correlation_matrix = self.calculate_correlation_matrix(user_id)

        #search browsing history
        search_history = self.browserHistory.loc[self.browserHistory['uid'] == user_id]['search'].values.tolist()
        similiar_products =[]
        for browsed_item in search_history:
            for product in self.productList:
                pname = product[1]
                pid = product[0]
                
                similarity = fuzz.token_set_ratio(browsed_item,pname)
                if similarity > 76:
                    similiar_products.append(pid)
        
        all_products_set = set()
        for product_id in similiar_products:
            product_corr = correlation_matrix[product_id]
            recommend_product = []
            for i in range(0,len(product_corr)):
                recommend_product.append([product_corr[i],i])
            recommend_product = sorted(product_corr,reverse=True)

            for i in range(0,5):
                all_products_set.add(recommend_product[i][1])
            
            all_product_list = []
            for index in all_products_set:
                all_product_list.append(self.productList[index])
            
            final_product_set = set()
            for i in range(0,min(len(all_product_list),10)):
                randNum = random.randint(0,len(all_product_list)-1)
                final_product_set.add(randNum)
            
            final_product_list = []
            for index in final_product_set:
                final_product_list.append(all_product_list[index])


            # for checking 
            for product in final_product_list:
                print("product = ", product)
            return final_product_list
        

        # Testing Purpose
        # def getUserOrderHistory(self,userId):
        #     orderHistory = self.orderDetails.loc[self.orderDetails['uid'] == userId].values.tolist()
        #     return orderHistory
    
        # def getUserBrowseHistory(self,userId):
        #     browseHistory = self.browserHistory.loc[self.browserHistory['uid'] == userId].values.tolist()
        #     return browseHistory
        