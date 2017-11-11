import click
import serial
import time

from codes import ports
from config import DefaultConfig
from log_config import log
from log_config import logging


def serial_setup():
    cfg = DefaultConfig()
    com = serial.Serial(**cfg)
    log.debug(com)
    com.flush()
    return com


def loglevelset(debug):
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)


def hdmi_input_control(port):
    com = serial_setup()
    code = ports['p0{0}'.format(int(port))]
    com.write(code)
    log.info('Activated port {0}'.format(int(port)))
    com.close()
