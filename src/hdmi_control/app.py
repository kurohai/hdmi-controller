#!/usr/bin/env python


import click
import serial
import time

from config import DevelopmentConfig
from config import SerialConfig
from logutil import get_logger
from models import Ports
from utils import set_log_debug
from utils import serial_setup


log = get_logger(__name__)


@click.group()
def cli():
    pass


@cli.command('test')
@click.option('--debug', '-d', is_flag=True, default=False)
def function_test(debug):
    log = set_log_debug(log, debug)
    com = serial_setup()
    ports = Ports()
    p = [v for k, v in ports.items() if k.startswith('p')]
    p.sort()
    log.debug(str(p))

    for k, v in enumerate(p):
        log.info('Switching to port: {0}'.format(k + 1))
        log.info('Using hex code: {0}'.format(v.encode('hex')))
        com.write(v)
        log.info(com.in_waiting)
        log.info(com.read(com.in_waiting).encode('hex'))
        time.sleep(2)
    com.close()


@cli.command('switch')
@click.argument('port')
@click.option('--debug', '-d', is_flag=True, default=False)
def hdmi_input_switch(port, debug):
    log = set_log_debug(log, debug)
    ports = Ports()
    com = serial_setup()
    com.reset_input_buffer()
    com.reset_output_buffer()
    code = ports.get_port_from_int(port)
    # code = ports['p0{0}'.format(int(port))]
    com.write(code)
    time.sleep(2)
    log.info('Activated port {0}'.format(code))
    log.debug(com.in_waiting)
    log.debug(com.read(com.in_waiting).encode('hex'))
    com.close()


@cli.command('reboot')
@click.option('--debug', '-d', is_flag=True, default=False)
def hdmi_device_reboot(debug):
    log = set_log_debug(log, debug)
    com = serial_setup()
    com.dsrdtr = True
    com.rtscts = True
    com.break_condition = True
    com.send_break()



@cli.command('hex')
@click.argument('porthex')
@click.option('--debug', '-d', is_flag=True, default=False)
def hdmi_hex(porthex, debug):
    log = set_log_debug(log, debug)
    com = serial_setup()
    ports = Ports()
    com.reset_input_buffer()
    com.reset_output_buffer()
    # code = ports['p0{0}'.format(int(port))]
    log.info('Sending cmd {0}'.format(code))
    code = ports.str_to_hex(porthex)
    com.write(code)
    time.sleep(2)
    log.info('Sent cmd {0}'.format(code))
    log.debug(com.in_waiting)
    log.debug(com.read(com.in_waiting).encode('hex'))
    com.close()


if __name__ == '__main__':
    cli()
