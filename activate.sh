#!/bin/bash

echo "Setting private environment..."
set -a
. env.sh
set +a

echo "Enabling virtualenv..."
pipenv shell
