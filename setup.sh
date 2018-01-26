#!/bin/bash


echo "Ensuring pipenv is installed..."
pip install --user pipenv > /dev/null

echo "Installing dependencies..."
pipenv --python 3.6 > /dev/null
pipenv install --ignore-pipfile > /dev/null

echo "Setting private environment..."
set -a
. env.sh
set +a

echo "Enabling virtualenv..."
pipenv shell
