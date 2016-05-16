#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hmac
import hashlib

def valid_origin(payload, supplied_hash, key):
	#TODO: validate webhook sender as noted in: https://sendgrid.com/blog/whats-webhook/#securingawebhook
	
	payload_as_string = dict_to_string(payload)

	computed_hash = hash_payload_to_github(payload_as_string, key)

	return hmac.compare_digest(hashed_payload, computed_hash)

def hash_payload_to_github(payload_as_string, key):
	#return hmac.new(payload_as_string, key, hashlib.sha1).hexdigest()
	return "sha1="+hmac.new(str(key), msg=payload_as_string, digestmod=hashlib.sha1).hexdigest()

def dict_to_string(di):
	return json.dumps(di)

def commit_is_shipshit(commit):
	if u'🚀💩' in commit["message"] or "shipshit" in commit["message"].lower():
		return True
	return False