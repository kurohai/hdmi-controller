#!/usr/bin/env python


import logging
import serial

from config import DevelopmentConfig
from config import SerialConfig
from logutils import get_logger
from models import Ports


log = get_logger(__name__)


def serial_setup():
    cfg = SerialConfig()
    log.info('setting up serial connection')
    com = serial.Serial(**cfg)
    log.debug(com)
    com.flush()
    return com


def loglevelset(log, debug):
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    return log


def hdmi_input_control(port):
    com = serial_setup()
    ports = Ports()
    code = ports.get_port_from_int(port)
    com.write(code)
    log.info('Activated port {0}'.format(code))
    com.close()
