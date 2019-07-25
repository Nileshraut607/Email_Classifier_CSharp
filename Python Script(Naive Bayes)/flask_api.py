
import os
import _pickle as c
from flask import Flask
from flask import request
from flask_cors import CORS

app=Flask('myApp')
model=c.load(open('pick_mod1.pkl','rb'))
CORS(app)

@app.route('/getPred', methods=['POST'])
def pred():
    data=request.form.get("#btn1");
    result=model.predict(data)
    return result
app.run(port=5000, debug=True)
