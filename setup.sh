#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "=====Setting up the autograder====="

echo "Initializing and updaing submodules..."
git submodule update --init --recursive

echo "Installing apt dependencies..."
apt-get install -y python3 python3-pip python3-dev

echo "Installing python3 dependencies..."
pip3 install -r $DIR/requirements.txt

echo "=====DONE!====="
