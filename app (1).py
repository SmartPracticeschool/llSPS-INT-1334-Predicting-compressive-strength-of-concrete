from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('Strength.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index1.html")
@app.route('/login',methods = ['post','get'])
def login():
    get_C = float(request.form['Cement'])
    get_BFS = float(request.form['Blast_Furnace_Slag'])
    get_FA = float(request.form['Fly_Ash'])
    get_W = float(request.form['Water'])
    get_S = float(request.form['Superplasticizer'])
    get_CA = float(request.form['Coarse_Aggregate'])
    get_F = float(request.form['Fine_Aggregate'])
    get_AD = float(request.form['Age_day'])
    
    final_data = [[get_C,get_BFS,get_FA,get_W,get_S,get_CA,get_F,get_AD]]
    y_pred = model.predict(np.array(final_data))
    return render_template("index1.html",show = str(y_pred[0]))


if __name__ =='__main__':
    app.run(debug = True)