# import flask dependencies
from flask import Flask, request, make_response, jsonify
import pprint as pp
import contexts
import sys

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def hello_world():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('parameters').get("pizza")

    # return a fulfillment response
    return {'fulfillmentText': u'La pizza qui vous intéresse est : '+str(action)}


# create a route for webhook
@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    # return response
    try:
      cntxt = contexts.Context( request )    
      response = cntxt.buildResponse()
      pp.pprint(response)
      return  make_response(jsonify( response ))
      #return make_response(jsonify(results()))
    except Exception as e:
      #e = sys.exc_info()[0]
      #print(f'-- ERROR --')
      #print(sys.exc_info()[1])
      pp.pprint( request.get_json() )
      raise
    

# run the app
if __name__ == '__main__':
   app.run(debug=True)