import json
import requests
from flask import Flask, jsonify , request
from flask_json import FlaskJSON, JsonError, json_response 
app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'firstname': 'Levent', 'lastname': 'Basaran'})

@app.route('/whoami' , methods=['GET'] )
def longword():

     firstname = request.args.get('firstname')
     lastname = request.args.get('lastname')

     result = { 'firstname' : firstname ,  'lastname' : lastname }

     return json.dumps(result) 

@app.route('/alert' , methods=['POST'] )
def err_to_json(ex):

    #return jsonify({"errors": }), 405



if __name__ == "__main__":
     
     app.run( debug=True, port=5000)