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

@app.errorhandler(405)
def resource_not_found(message):
    return jsonify(message=str(message))

@app.route('/alert', methods=['POST'])
def get_one_cheese():
    return jsonify(message)



if __name__ == "__main__":
     
     app.run( debug=True, port=5000)
