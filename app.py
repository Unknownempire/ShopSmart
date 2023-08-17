from flask import Flask, request, jsonify,render_template

# from Recommender1 import Recommender
from recommender import Recommender
from NewRecommendation import user_similarity
import os
import random

app = Flask(__name__)



# Call Recommender init here. Training yaha hogayi server chalte hi.
# Routes me use Recommender ka getRecommendation function, ye instantly return karega

# Pickle file 
import pickle
with open("recommender_pickel.txt",'rb') as f:
    a=pickle.load(f)
    
# JS calls Flask, Flask me routes h jisme we send recommendations, update/insert/edit dataset ( jaha pe bhi wo hosted h )
REC = Recommender()
User_Simi=user_similarity()
# userId = random.randint(1,500)
# print('userid = ', userId)
userId=46
@app.route('/productRecommendation', methods=['GET'])
def getRecommendations():
    if request.method == 'GET':
        # userId = request.args.get('userId')
        if userId != None:
            recommendations = REC.calculate_product_Recommendation(int(userId))
        # print(recommendations)
        return jsonify(recommendations)


@app.route('/getProductList', methods=['GET'])
def getProductList():
    if request.method == 'GET':
        return jsonify(REC.productList)


@app.route('/getUserOrderHistory', methods=['GET'])
def getUserOrderHistory():
    if request.method == 'GET':
        # userId = request.args.get('userId')
        orderHist = REC.getUserOrderHistory(int(userId))
        return jsonify(orderHist)


@app.route('/getUserBrowseHistory', methods=['GET'])
def getUserBrowseHistory():
    if request.method == 'GET':
        # userId = request.args.get('userId')
        browseHist = REC.getUserBrowseHistory(int(userId))
        return jsonify(browseHist)

@app.route('/UserSim', methods=['GET'])
def UserSim():
        if request.method == 'GET':
        # userId = request.args.get('userId')
            if userId != None:
                us=User_Simi.get_Recommendation(int(userId))
        # print(recommendations)
            return jsonify(us)
        # userId = request.args.get('userId', type=int)  # Get userId from request arguments
        # us=User_Simi.get_Recommendation(userId)
        # return jsonify(us)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/front')
def front():
    return render_template('front.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

PORT = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=True)
    

