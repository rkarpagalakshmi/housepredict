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
       SQUARE_FT = request.form["SQUARE_FT"]
       SQUARE_FT = int(SQUARE_FT)
       print(SQUARE_FT)
       READY_TO_MOVE = request.form["READY_TO_MOVE"]
       READY_TO_MOVE = int(READY_TO_MOVE)
       print(READY_TO_MOVE)
       RESALE = request.form["RESALE"]
       RESALE = int(RESALE)
       print(RESALE)
       LONGITUDE = request.form["LONGITUDE"]
       LONGITUDE = int(LONGITUDE)
       print(LONGITUDE)
       LATITUDE = request.form["LATITUDE"]
       LATITUDE = int(LATITUDE)
       print(LATITUDE)
       BHK_NO = request.form["BHK_NO"]
       BHK_NO = int(BHK_NO)
       print(BHK_NO)
       price =  model.predict([[SQUARE_FT,READY_TO_MOVE,RESALE,LONGITUDE,LATITUDE, BHK_NO] ])
       print("price",price)
       return render_template('index.html', prediction_price='price = {}'.format(price))
       #return render_template('index.html')


if __name__ == "__main__":
    app.run(debug='True')