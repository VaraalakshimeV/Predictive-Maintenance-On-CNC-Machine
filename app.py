from flask import Flask,render_template,url_for,request
from flask_material import Material

# EDA PKg
import pandas as pd 
import numpy as np 
import sklearn
import pickle


app = Flask(__name__)
Material(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/class_0.html')
def class_0():
    return render_template("class_0.html")
@app.route('/class_1.html')
def class_1():
    return render_template("class_1.html")
@app.route('/class_2.html')
def class_2():
    return render_template("class_2.html")
@app.route('/',methods=["POST"])
def analyze():
	if request.method == 'POST':
		Spindle_Motor_Baselooseness_Vibration	 = request.form['Spindle_Motor_Baselooseness_Vibration']
		Spindle_Motor_Bearing_Vibration = request.form['Spindle_Motor_Bearing_Vibration']
		Spindle_Motor_Misalignment_Vibration = request.form['Spindle_Motor_Misalignment_Vibration']
		Spindle_Motor_Unbalance_Vibration = request.form['Spindle_Motor_Unbalance_Vibration']
		model=pd.read_pickle('data/mlp_clf.pkl') 
           

		# Clean the data by convert from unicode to float 
		sample_data = [Spindle_Motor_Baselooseness_Vibration,Spindle_Motor_Bearing_Vibration,Spindle_Motor_Misalignment_Vibration,Spindle_Motor_Unbalance_Vibration]
		clean_data = [float(i) for i in sample_data]

		# Reshape the Data as a Sample not Individual Features
		ex1 = np.array(clean_data).reshape(1,-1)
		result_prediction = model.predict(ex1)

	return render_template('index.html', Spindle_Motor_Baselooseness_Vibration=Spindle_Motor_Baselooseness_Vibration,
		Spindle_Motor_Bearing_Vibration=Spindle_Motor_Bearing_Vibration,
		Spindle_Motor_Misalignment_Vibration=Spindle_Motor_Misalignment_Vibration,
		Spindle_Motor_Unbalance_Vibration=Spindle_Motor_Unbalance_Vibration,
		clean_data=clean_data,
		result_prediction=result_prediction)
      
	  
@app.route('/',methods=["POST"])
def predict():
     model=pd.read_pickle('data/mlp_clf.pkl')
     int_features=[int(x) for x in request.form.values()]
     final=[np.array(int_features)]
     print(int_features)
     print(final)
     prediction=model.predict_proba(final)
     return render_template('index.html', result_prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)