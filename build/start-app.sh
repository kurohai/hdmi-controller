#!/bin/bash

cd /home/pi/hdmi-controller

workon hdmi-control-ui

pip install -r ./requirements.txt

./run.sh
