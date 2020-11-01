from flask import Flask, request,render_template
import joblib
import numpy as np 

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def hello():
     return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
       POSTED_BY_Builder = request.form["POSTED_BY_Builder"]
       POSTED_BY_Builder = int(POSTED_BY_Builder)
       print(POSTED_BY_Builder)
       POSTED_BY_Dealer = request.form["POSTED_BY_Dealer"]
       POSTED_BY_Dealer = int(POSTED_BY_Dealer)
       print(POSTED_BY_Dealer)
       POSTED_BY_Owner = request.form["POSTED_BY_Owner"]
       POSTED_BY_Owner = int(POSTED_BY_Owner)
       print(POSTED_BY_Owner)
       RERA = request.form["RERA"]
       RERA = int(RERA)
       print(RERA)
       SQUARE_FT = request.form["SQUARE_FT"]
       SQUARE_FT = int(SQUARE_FT)
       print(SQUARE_FT)
       READY_TO_MOVE = request.form["READY_TO_MOVE"]
       READY_TO_MOVE = int(READY_TO_MOVE)
       print(READY_TO_MOVE)
       LONGITUDE = request.form["LONGITUDE"]
       LONGITUDE = int(LONGITUDE)
       print(LONGITUDE)
       LATITUDE = request.form["LATITUDE"]
       LATITUDE = int(LATITUDE)
       print(LATITUDE)
       BHK_NO = request.form["BHK_NO"]
       BHK_NO = int(BHK_NO)
       print(BHK_NO)
       price =  model.predict([[POSTED_BY_Builder,POSTED_BY_Dealer, POSTED_BY_Owner, RERA,SQUARE_FT,READY_TO_MOVE,LONGITUDE,LATITUDE, BHK_NO] ])
       print("price",price)
       return render_template('index.html', prediction_price='price = {}'.format(price))
       #return render_template('index.html')


if __name__ == "__main__":
    app.run(debug='True')