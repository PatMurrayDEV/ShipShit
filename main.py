#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports the Flask wrapper, abort function and request context
from flask import Flask, abort, request

from werkzeug.contrib.cache import SimpleCache

#Create a little persistent cache object, just for example's sake
cache = SimpleCache()

#Import some helper functions
from webhook_utils import valid_origin
import settings
from github_interface import GithubClient

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

	if request.method != 'POST':
		abort(405)

	#This is actually a valid webhook, so process it!

	event_type = request.headers.get('X-GitHub-Event')

	if event_type != "push":
		#We only support push events!
		abort(501)

	#You can use this handy method inside the request to get the POSTed JSON
	webhook_payload = request.get_json()

	cache.set('webhook_payload', webhook_payload)

	for commit in webhook_payload["commits"]:
		if u'🚀💩' in commit["message"] or "shipshit" in commit["message"].lower():
			#Create a new issue
			client = GithubClient(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)
			response = client.create_issue('New shipshit issue', 
				'This is an automatically created shipshit issue',
				webhook_payload["repository"]["owner"]["name"],
				webhook_payload["repository"]["name"],
				)
			if not response:
				abort(500)

	return 'Successful push'


@app.route("/past-webhook")
def past_webhook():
	#This is a really naive implementation of getting and displaying a past webhook's data
	return """
	%s
	"""  % cache.get('webhook_payload')

# Ridiculously simplistic running mechanism
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=settings.PORT, debug=settings.DEBUG_ON)