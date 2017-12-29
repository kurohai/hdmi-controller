#!/bin/bash

mkdir -p $LOG_DIR
mkdir -p $PID_DIR
# echo ${MAINPID} > ${PIDFile}

for f in $CONFIG_DIR/*.tunnel;
do
    echo "running $f"
    $f;
done
