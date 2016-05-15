#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import webhook_utils

class TestWebhookMethods(unittest.TestCase):

	def test_shipshit_text(self):
		sample_commit = {
			"message": "here's some shipshit"
		}
		result = webhook_utils.commit_is_shipshit(sample_commit)
		self.assertTrue(result)

	def test_shipshit_emoji(self):
		sample_commit = {
			"message": u'this is really shit 🚀💩'
		}
		result = webhook_utils.commit_is_shipshit(sample_commit)
		self.assertTrue(result)

	def test_not_shipshit_text(self):
		sample_commit = {
			"message": "this is sure some top quality code"
		}
		result = webhook_utils.commit_is_shipshit(sample_commit)
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()