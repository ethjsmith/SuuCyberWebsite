from flask import Flask,redirect
from flask_basicauth import BasicAuth
import subprocess, os, requests

folder = os.path.dirname(os.path.realpath(__file__))
# Path should be variable or something
app = Flask(__name__,static_url_path='',static_folder=folder)


@app.route('/')
def main():
	return app.send_static_file('/home/ejsmith/Documents/suucyberwebsite/index.html')


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
