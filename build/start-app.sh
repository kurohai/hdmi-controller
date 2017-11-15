#!/bin/bash

cd /home/pi/hdmi-controller

sudo pkill -9 -f "/usr/bin/uwsgi --ini ./uwsgi-hdmi-control-ui-devel.ini"
workon hdmi-control-ui

$VIRTUAL_ENV/bin/pip install -r ./requirements.txt

./run.sh
