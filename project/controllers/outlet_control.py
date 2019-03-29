# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask_wtf import FlaskForm
from project import app
from project import hdmi_input_control
from wtforms import StringField
from wtforms.validators import DataRequired
# from loguitl import get_logger


ports = [i + 1 for i in xrange(8)]


class CreateForm(FlaskForm):
    text = StringField('name', validators=[DataRequired()])

bp = Blueprint('outlets', __name__, url_prefix='/outlets')

@bp.route('/')
def start():

    return render_template('public/index.html', ports=ports)


def format_api_string(command):
    cmd = command.strip()
    cmd = cmd.lower()
    cmd = cmd.replace('_', '-')
    cmd = cmd.replace(' ', '-')
    return cmd


def _outlet_power_toggle(outlet_name, command, switch):
    import requests
    outlet_power_api_url = 'https://mcp.kurohai.com/api/v1/outlets/[[name]]/control/[[state]]/'
    outlet_status_api_url = 'https://mcp.kurohai.com/api/v1/outlets/[[name]]/status/'
    result = requests.get(outlet_power_api_url)
    return result


@bp.route('/outlet/', methods=['GET', 'POST'])
@bp.route('/outlet/<name>/', methods=['GET', 'POST'])
def outlet_get(name=None):
    if name is None:
        pass
    return {}

@bp.route('/outlet/<name>/<command>/<switch>/', methods=['GET', 'POST'])
def outlet_power_toggle(name, command, switch=1):

    command = format_api_string(command)
    name = format_api_string(name)

    print(name, command, switch)

    result = _outlet_power_toggle(name, command, switch)

    if result.ok:
        data = {'status': 'success', 'outlet': name, 'switch': switch, 'state': result.json()['status']}
        return jsonify(data)
    else:
        data = {'status': 'error', 'outlet': name, 'switch': switch}
        return jsonify(data)
