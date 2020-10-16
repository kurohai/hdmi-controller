# -*- coding: utf-8 -*-
__version__ = '0.1'

mcp_api_url = 'https://mcp.kurohai.com/api/v1'
outlet_power_api_url_template = '{base}/outlets/[[name]]/control/[[state]]/'.format(base=mcp_api_url)
outlet_status_api_url_template = '{base}/outlets/[[name]]/status/'.format(base=mcp_api_url)


from flask import Flask
from flask import redirect
from flask import request
from flask_debugtoolbar import DebugToolbarExtension

def create_app(config='default'):
    app = Flask('project')
    app.config['SECRET_KEY'] = 'random'
    app.debug = True
    toolbar = DebugToolbarExtension(app)
    return app

from controller import hdmi_input_control
from .logutil import get_logger


log = get_logger(__name__)


def _check_path(url):
    if not url.endswith('/') and not url.endswith('.json'):
        return True
    else:
        return False

app = create_app()
@app.before_request
def add_trailing():
    rp = request.path
    log.debug('pre-path: {0}'.format(rp))
    log.debug('method: {0}'.format(request.method))
    log.debug('post-path: {0}'.format(str(request.path)))

    if _check_path(rp):
        return redirect(rp + '/')

    # if not rp.endswith('/'):
    #     return redirect(rp + '/')

from project.controllers import hdmi_bp
from project.controllers import outlet_bp

log.info('registering hdmi blueprint...')
app.register_blueprint(hdmi_bp)
log.info('registering outlet blueprint...')
app.register_blueprint(outlet_bp)
log.info('All blueprints registered!')
