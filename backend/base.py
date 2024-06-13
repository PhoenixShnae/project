from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/data',methods=['POST'])
def submit():
    data= request.json
    if not data:
        return jsonify(error="Keyword not there!"),400
    print (data)

    with open("textdata.txt", 'r') as file:
        multiline_string = file.read()
    html_string=multiline_string.replace('\n','"0')
    
    test_string = """hello
    fhfggfhhe
    exxxxe"""
    return test_string

if __name__ == "__main__":
    app(debug=True)