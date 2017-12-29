#!/bin/bash

cd /home/pi/hdmi-controller

sudo pkill -9 -f ".*/uwsgi --ini ./uwsgi.*.ini"
# workon hdmi-control-ui

# $VIRTUAL_ENV/bin/pip install -r ./requirements.txt

./run.sh
