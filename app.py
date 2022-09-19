from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("dnn.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":            
      
        airline=request.form['airline']     
        if (airline=='Airline_Air_Asia'):            
            Airline_Air_Asia = 1
            Airline_Air_India = 0
            Airline_IndiGo =0
        
        elif (airline=='Airline_Air_India'):            
            Airline_Air_Asia = 0
            Airline_Air_India = 1    
            Airline_IndiGo = 0     
        
        elif (airline=='Airline_IndiGo'):            
            Airline_Air_Asia = 0
            Airline_Air_India = 0   
            Airline_IndiGo = 1  
            
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        elif (Source == 'Chennai'):
             Source_Delhi = 0
             Source_Kolkata = 0
             Source_Mumbai = 0
             Source_Chennai = 1

        else:
             Source_Delhi = 0
             Source_Kolkata = 0
             Source_Mumbai = 0
             Source_Chennai = 0
        
        prediction=model.predict([[                 
            
            Source_Delhi,
            Source_Kolkata,
            Source_Mumbai,
            Source_Chennai,
            Airline_Air_Asia,
            Airline_Air_India,    
            Airline_IndiGo
            
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
