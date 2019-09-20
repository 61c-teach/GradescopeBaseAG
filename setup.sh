#!/bin/bash

mkdir -p /root/.ssh
cat ssh_config >> /root/.ssh/config
cp GradescopeBase_deploy_key /root/.ssh/GradescopeBase_deploy_key

git submodule update --init --recursive

apt-get install -y python3 python3-pip python3-dev
pip3 install -r /autograder/root/requirements.txt