# Imports the Flask wrapper, abort function and request context
from flask import Flask, abort, request

from werkzeug.contrib.cache import SimpleCache

#Create a little persistent cache object, just for example's sake
cache = SimpleCache()

from webhook_utils import valid_origin


import os

port = int(os.environ.get('PORT', 5000))


# Creates an instance of the flask server using *this* module as its unique identifier
app = Flask(__name__)

#This is a function decorator, it basically is a middleware that attaches the function hello to the flask gateway
@app.route("/")
def home():
	return "Hello world"

@app.route("/webhook", methods=['GET', 'POST'])
def webhook_receipt():

	if not valid_origin():
		abort(403)

	if request.method == 'GET':
		return ''

	if request.method == 'POST':
		#This is actually a valid webhook, so process it!

		#You can use this handy method inside the request to get the POSTed JSON
		webhook_data = request.get_json()

		cache.set('webhook_data', webhook_data)

		return 'SUCCESS'


@app.route("/past-webhook")
def past_webhook():
	#This is a really naive implementation of getting and displaying a past webhook's data
	return """
	%s
	"""  % cache.get('webhook_data')

# Ridiculously simplistic running mechanism
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)