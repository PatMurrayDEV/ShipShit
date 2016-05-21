#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import hmac
import hashlib

def valid_origin(payload, supplied_hash, key):
	"""
		Calculates the hash of the payload using the supplied key, and
		compares it using the supplied hash to determine whether
		the webhook payload is from GitHub

		Parameters
		----------
		payload : String
			A GitHub payload in string form
		supplied_hash : String
			A hashed version of the payload from the webhook source
		key : String
			The key to use to hash the payload
		Returns
		-------
		bool
			Whether or not the webhook payload is in fact from a trusted origin


	"""
	if not key:
		return True

	computed_hash = hash_payload_to_github(payload, key)
	return hmac.compare_digest(str(supplied_hash), str(computed_hash))


def hash_payload_to_github(payload_as_string, key):
	"""
	Performs the hashing of a payload with a given key, uses SHA1 encryption
	"""
	return "sha1="+hmac.new(bytes(key), msg=payload_as_string, digestmod=hashlib.sha1).hexdigest()

def dict_to_string(di):
	return json.dumps(di)

def commit_is_shipshit(commit):
	"""
		Takes a GitHub commit object and checks whether the commit message is shipshit

		Parameters
		----------
		commit : Dictionary
			The commit in question

		Returns
		-------
		bool
			Whether or not it's shipshit

	"""
	if u'🚀💩' in commit["message"] or "shipshit" in commit["message"].lower():
		return True
	return False