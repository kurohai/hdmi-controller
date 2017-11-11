#!/bin/bash

# export PATH=$PATH:$VIRTUAL_ENV/bin

# source ~/.bashrc


echo $PYTHONPATH

sudo -E $VIRTUAL_ENV/bin/uwsgi --ini ./uwsgi-hdmi-control-ui-devel.ini
