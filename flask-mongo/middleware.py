import coverage

from werkzeug.wrappers import Request
from utils import write_dedup

class CoverageMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        id = req.headers.get('KEPLOY-TEST-ID')
        if id == None:
            return self.app(environ, start_response)
        cov = coverage.Coverage(cover_pylib=False)
        cov.start()
        response = self.app(environ, start_response)
        cov.stop()
        result = cov.get_data()
        write_dedup(result, id)
        return response
