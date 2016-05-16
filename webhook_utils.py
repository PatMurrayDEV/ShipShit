#!/usr/bin/env python
# -*- coding: utf-8 -*-

def valid_origin():
	#TODO: validate webhook sender as noted in: https://sendgrid.com/blog/whats-webhook/#securingawebhook
	return True
	
def commit_is_shipshit(commit):
	if u'🚀💩' in commit["message"] or "shipshit" in commit["message"].lower():
		return True
	return False