#!/usr/bin/env python


import logging
import serial

from munch import Munch


class BaseConfig(Munch):
    """docstring for BaseConfig"""

    def __init__(self, *args, **kwargs):
        super(BaseConfig, self).__init__(*args, **kwargs)
        self.loglevel = logging.INFO


class DevelopmentConfig(BaseConfig):
    """docstring for DevelopmentConfig"""

    def __init__(self, *args, **kwargs):
        super(DevelopmentConfig, self).__init__(*args, **kwargs)
        self.loglevel = logging.DEBUG


class SerialConfig(BaseConfig):
    """docstring for SerialConfig"""

    def __init__(self, *args, **kwargs):
        super(SerialConfig, self).__init__(*args, **kwargs)
        self.port = '/dev/ttyUSB0'
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.stopbits = serial.STOPBITS_ONE
        self.parity = serial.PARITY_NONE
