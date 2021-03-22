import json
import requests
import os
from flask import Flask, jsonify , request
from flask_json import FlaskJSON, JsonError, json_response 


app = Flask(__name__)

#env_var = os.environ 
#os.environ['webhook_url'] = 'https://webhook.site/52a618cb-0f1e-4ac7-8b16-4b64b295f932'

#data = { 'message': 'http://127.0.0.1:5000/alert' }








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
   if request.method == 'POST':
     r = requests.post(os.environ['webhook_url'], request.json, headers={'Content-Type': 'application/json'})
     print("received data: ", request.json)
    
     return 'success', 200
   else:
    
      abort(400)


if __name__ == "__main__":
     
     app.run( debug=True, port=5000)
