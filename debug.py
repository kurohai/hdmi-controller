from gevent.wsgi import WSGIServer
from project import app
from werkzeug.serving import run_with_reloader


@run_with_reloader
def run_server():
    # Run this as production dev server
    hs = WSGIServer(('', 5000), app)
    hs.serve_forever()


if __name__ == '__main__':
    run_server()
