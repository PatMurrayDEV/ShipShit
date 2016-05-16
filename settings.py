#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

PORT = int(os.environ.get('PORT', 5000))

DEBUG_ON = bool(os.environ.get('DEBUG', False))

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', '')

GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD', '')

GITHUB_WEBHOOK_SECRET = os.environ.get('GITHUB_WEBHOOK_SECRET', None)