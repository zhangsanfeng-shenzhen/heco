#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import json
import random
import requests

HOST = 'https://http-mainnet-node.huobichain.com'

class AuthService(object):
	def __init__(self, host = None):
		if host is None:
			host = HOST
		self.host = host
		self.header = {
			'Content-Type': 'application/json',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
		}

	def call(self, *args):
		payload = {
			'jsonrpc': '2.0', 
			'method': self.name,
			'id' : random.randint(0, 1000),
			'params': args
		}
		data = json.dumps(payload)
		print(data)
		post = requests.post(self.host, headers=self.header, data = data , timeout=(2,5))
		print(post.text)
		return post.text

	def __getattr__(self, name):
		if name.startswith('__') and name.endswith('__'):
			raise AttributeError
		self.name = name
		return self.call

'''
auth = AuthService("HH")
versin = auth.eth_protocolVersion()
balance = auth.eth_getBalance('0x407d73d8a49eeb85d32cf465507dd71d507100c1','latest')
'''



