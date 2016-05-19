#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import json
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

	def test_json_dump_should_not_raise_exception_emoji(self):
		try:
			sample_commit = {
				"message": "this is  🚀💩"
			}
			result = webhook_utils.dict_to_string(sample_commit)
		except Exception:
			self.fail("stringifying should not have raised an exception!")

	def test_hash_sample_payload(self):
		sample_supplied_hash = "sha1=1cfa9f7b83c5cda3fcc5ae9f29b4e93b04aec251"
		sample_payload = file('sample_payload.json').read()
		sample_key = 'youjustgotsnailedlol'
		
		computed_hash = webhook_utils.hash_payload_to_github(sample_payload, sample_key)

		self.assertEqual(sample_supplied_hash, computed_hash)
	def test_hash_comparison(self):
		sample_supplied_hash = "sha1=1cfa9f7b83c5cda3fcc5ae9f29b4e93b04aec251"
		sample_payload = file('sample_payload.json').read()
		sample_key = 'youjustgotsnailedlol'
		is_valid = webhook_utils.valid_origin(sample_payload, sample_supplied_hash, sample_key)

		self.assertTrue(is_valid)

	def test_hash_comparison_fail(self):
		sample_supplied_hash = "sha1=1cfa9f7b83c5cda3fcc5ae9f29b4e93b04aec253"
		sample_payload = file('sample_payload.json').read()
		sample_key = 'youjustgotsnailedlol'
		should_not_be_valid = webhook_utils.valid_origin(sample_payload, sample_supplied_hash, sample_key)

		self.assertFalse(should_not_be_valid)
if __name__ == '__main__':
	unittest.main()