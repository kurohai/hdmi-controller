#!/bin/bash

# export PATH=$PATH:$VIRTUAL_ENV/bin

# source ~/.bashrc


echo $PYTHONPATH

sudo -E /usr/bin/uwsgi --ini ./uwsgi-hdmi-controller-devel.ini
