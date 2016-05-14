#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#We will create our own GitHub interface because existing libraries 
#don't support what we want.

class GithubClient:
	def __init__(self, username, password, baseurl="https://api.github.com"):
		self.username = username
		self.password = password
		self.baseurl = baseurl
	def create_issue(self, title, owner, repo, body):
		#TODO: confirm enterprise github support
		request_url = '%s/repos/%s/%s/issues' % (self.baseurl, owner, repo)
		request_payload = {
			"title": title,
			"body": body,
		}
		r = requests.post(request_url, 
			auth=(self.username, self.password),
			json=request_payload
		)
		return r.json()

