from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('http://localhost:5000/data',methods=['POST'])
def submit():
    data= request.json
    if not data:
        return jsonify(error="Keyword not there!"),400
    print (data)
    return jsonify(data)