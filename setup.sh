#!/bin/bash
#/*
# * @Author: ThaumicMekanism [Stephan K.] 
# * @Date: 2020-01-23 21:05:45 
# * @Last Modified by:   ThaumicMekanism [Stephan K.] 
# * @Last Modified time: 2020-01-23 21:05:45 
# */
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
