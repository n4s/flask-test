#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
	return "<h1>Hello World</h1>\nHello World\n"
