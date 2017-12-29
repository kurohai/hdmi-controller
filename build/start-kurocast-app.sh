#!/bin/bash

cd /mnt/data/code/kurocast
echo "my post curdir: $PWD"

# sudo pkill -9 -f ".*/uwsgi --ini ./uwsgi.*.ini"
# workon hdmi-control-ui


# $VIRTUAL_ENV/bin/pip install -r ./requirements.txt

chmod +x ./run.sh

./run.sh
