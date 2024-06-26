from flask import Flask, render_template, jsonify,request
import os
import yaml 
import joblib 
import numpy as np 
from prediction_service import prediction
params_path = "params.yaml" 
webapp_root = "webapp" 

static_dir = os.path.join(webapp_root,"static")
template_dir = os.path.join(webapp_root,"templates")

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)



@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                response = prediction.form_response(dict_req)
                return render_template("index.html", response=response)
            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

            return render_template("404_error.html", error=error)
    else: 
        return render_template("index.html")
if __name__=="__main__":
    app.run(port=5000,debug=True)