#!/bin/bash

# this script is WIP, I think python ships with pip automatically these days, so this might be unnessesary
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

sudo apt update
sudo apt install curl python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv nginx

python get-pip.py

pip install Flask
pip install Flask-BasicAuth
