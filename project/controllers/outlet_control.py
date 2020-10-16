#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys

from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session, g
from flask_wtf import FlaskForm
from pprint import pprint
from project import app
from project import hdmi_input_control
from project import get_logger
from wtforms import StringField
from wtforms.validators import DataRequired
import requests
from munch import Munch, munchify

log = get_logger(__name__)

ports = [i + 1 for i in xrange(8)]


class CreateForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])

bp = Blueprint('outlets', __name__, url_prefix='/outlets')

outlet_base_api_url = 'https://mcp.kurohai.com/api/v1/outlets/'
outlet_power_api_url = 'https://mcp.kurohai.com/api/v1/outlets/[[name]]/control/[[state]]/[[switch]]'
outlet_status_api_url = 'https://mcp.kurohai.com/api/v1/outlets/[[name]]/status/'

@bp.route('/')
def start():
    return render_template('public/outlet-power.html', ports=ports)


def format_api_string(command):
    cmd = command.strip()
    cmd = cmd.lower()
    cmd = cmd.replace('_', '-')
    cmd = cmd.replace(' ', '-')
    return cmd


def _outlet_power_toggle(outlet_name, command, switch):
    url = outlet_power_api_url.replace('[[name]]', outlet_name)
    url = url.replace('[[state]]', command)
    url = url.replace('[[switch]]', switch)
    log.info('url: {0}'.format(url))
    result = requests.get(url)
    return result


def _get_outlets():
    url = outlet_base_api_url
    log.info('url: {0}'.format(url))
    result = requests.get(url)
    log.info('result: {0}'.format(result.content))
    return result

def _outlets_in_session(outlets):
    all_outlets = Munch()

    for outlet in outlets.json():
        log.info(outlet)
        all_outlets[outlet['name']] = outlet
    session.outlets = all_outlets

@bp.route('/outlet/', methods=['GET', 'POST'])
@bp.route('/outlet/<name>/', methods=['GET', 'POST'])
def outlet_get(name=None):
    if name is None:
        # if 'outlets' in session:
        #     all_outlets = session.outlets
        # else:
        #     all_outlets = Munch()
        # all_outlets = Munch()
        log.info('all outlets: {0}'.format(all_outlets))
        # all_outlets = Munch()
        outlets = _get_outlets()
        _outlets_in_session(outlets)
        # for outlet in outlets.json():
        #     log.info(outlet)
        #     all_outlets[outlet['name']] = outlet
        # session.outlets = all_outlets
            # for k, v in outlet.items():
                # all_outlets[]

        return jsonify(session.outlets)

    return jsonify({'error': 'derp'})


@bp.route('/outlet/<name>/<command>/<switch>/', methods=['GET', 'POST'])
def outlet_power_toggle(name, command, switch=1):

    command = format_api_string(command)
    name = format_api_string(name)

    print(name, command, switch)
    log.info(name, command, switch)

    result = _outlet_power_toggle(name, command, switch)

    if result.ok:
        data = {'status': 'success', 'outlet': name, 'switch': switch, 'state': result.json()['status']}
        return jsonify(data)
    else:
        data = {'status': 'error', 'outlet': name, 'switch': switch}
        return jsonify(data)


@bp.route('/view/')
def all_outlets_view():
    if 'outlets' not in session:
        outlets = _get_outlets()
        _outlets_in_session(outlets)
    return render_template('public/outlet-power.html', outlets=session.outlets)
