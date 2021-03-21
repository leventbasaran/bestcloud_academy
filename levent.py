import json
import requests
from flask import Flask, jsonify , request
from flask_json import FlaskJSON, JsonError, json_response 
app = Flask(__name__)


webhook_url = 'https://webhook.site/17b407f8-5266-4e83-8305-57d60136995e'

data = { 'message': 'http://127.0.0.1:5000/alert' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})



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
    
     print("received data: ", request.json)
    
     return 'success', 200
  else:
    
      abort(400)



if __name__ == "__main__":
     
     app.run( debug=True, port=5000)
