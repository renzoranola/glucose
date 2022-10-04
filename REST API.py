from flask import Flask, jsonify, request

import json

app = Flask(__name__)

glucose = [
    {
        "glucose_id": 1,
        "date" : "April/9/2020",
        "glucose" : "200mg/dL"
    },
    {
        "glucose_id": 2,
        "date" : "May/13/2020",
        "glucose" : "140mg/dL"
    }
]
# get all in the dictonary
@app.route('/glucose/get', methods=['GET'])
def get_glucoses():
    return jsonify(glucose)
    
# get specific in the dictionary
@app.route('/glucose/<int:glucose_id>', methods=['GET'])
def get_glucose(glucose_id):
    id = [ glucose[glucose_id-1] ]
    return jsonify({"glucose":id})


if __name__== '__main__':
    app.run()