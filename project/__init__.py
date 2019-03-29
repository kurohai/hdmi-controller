# -*- coding: utf-8 -*-
__version__ = '0.1'

mcp_api_url = 'https://mcp.kurohai.com/api/v1'
outlet_power_api_url_template = '{base}/outlets/[[name]]/control/[[state]]/'.format(base=mcp_api_url)
outlet_status_api_url_template = '{base}/outlets/[[name]]/status/'.format(base=mcp_api_url)


from flask import Flask
from flask import redirect
from flask import request
# from flask_debugtoolbar import DebugToolbarExtension
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
# toolbar = DebugToolbarExtension(app)
from controller import hdmi_input_control
from project.controllers import *
from project.controllers import hdmi_bp
from project.controllers import outlet_bp


@app.before_request
def add_trailing():
    rp = request.path
    if not rp.endswith('/'):
        return redirect(rp + '/')





app.register_blueprint(hdmi_bp)
app.register_blueprint(outlet_bp)
