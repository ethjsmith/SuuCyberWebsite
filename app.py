from flask import Flask,redirect
from flask_basicauth import BasicAuth
import subprocess, os, requests


# Path should be variable or something
app = Flask(__name__,static_url_path='/home/ejsmith/Documents/suucyberwebsite')

@app.route('/')
def main():
	return app.send_static_file('index.html')


if __name__ == "__main__":
	app.run()
