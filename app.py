from flask import Flask,request
from flask_cors import CORS, cross_origin
import diabetes
app=Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/diabetes",methods=['GET','POST'])

def baseRoute():
    if request.method=='GET':
        return "You have reached the server"
    elif request.method=='POST':
        response=request.get_json()
        glucose=response['glucose']
        blood=response['bloodPressure']
        skin=response['skinFold']
        insulin=response['insulin']
        bmi=response['bmi']
        my_dict = {"B":float(glucose), "C":float(blood),"D":float(skin), "E":float(insulin), "F": float(bmi)}
        output = diabetes.check_input(my_dict)
        print("Output :",output)
        res_data={}
        if output==0:
            res_data['diabetes']=True
            return res_data
        else:
            res_data['diabetes']=False
            return res_data


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)
