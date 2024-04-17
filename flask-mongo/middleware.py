import coverage

class CoverageMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        cov = coverage.Coverage(cover_pylib=False)
        cov.start()
        response = self.app(environ, start_response)
        cov.stop()
        result = cov.get_data()
        for file in result.measured_files():
            print(file, result.lines(file))

        return response
