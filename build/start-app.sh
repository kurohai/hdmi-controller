#!/bin/bash

cd /mnt/data/code/media-voice-control

sudo pkill -9 -f ".*/uwsgi --ini ./uwsgi.*.ini"
# workon hdmi-control-ui

# $VIRTUAL_ENV/bin/pip install -r ./requirements.txt

./run.sh
