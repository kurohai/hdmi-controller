#!/bin/bash

NAME=`basename $0`
PIDFILE=${PID_DIR}/${NAME}.pid
SCRIPTNAME=/etc/init.d/${NAME}
PORT=9801

export AUTOSSH_PORT=${PORT}
export AUTOSSH_PIDFILE=${PIDFILE}
export AUTOSSH_LOGLEVEL=7
export AUTOSSH_LOGFILE=${LOG_DIR}/${NAME}.log


/usr/lib/autossh/autossh -M ${PORT} -f -i ${RSA_KEY} -nNTfR 9001:localhost:9001  root@kurohai.com

