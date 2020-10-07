import os
from io import BytesIO
from flask import Flask
from flask_cors import CORS

import requestbin.config as config
from requestbin.filters import (approximate_time, exact_time, friendly_size,
                                friendly_time, short_date, status_class, to_qs)
from werkzeug.middleware.proxy_fix import ProxyFix


class MyApplication(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsgi_app = WSGIRawBody(ProxyFix(self.wsgi_app))
        self.add_config()
        self.add_filters()

    def add_config(self):
        self.debug = config.DEBUG
        self.secret_key = config.FLASK_SESSION_SECRET_KEY
        self.root_path = os.path.abspath(os.path.dirname(__file__))
        if config.BUGSNAG_KEY:
            import bugsnag
            from bugsnag.flask import handle_exceptions
            bugsnag.configure(
                api_key=config.BUGSNAG_KEY,
                project_root=self.root_path,
                # 'production' is a magic string for bugsnag, rest are arbitrary
                release_stage=config.REALM.replace("prod", "production"),
                notify_release_stages=["production", "test"],
                use_ssl=True
            )
            handle_exceptions(self)
        if os.environ.get('ENABLE_CORS', config.ENABLE_CORS):
            _ = CORS(
                self,
                resources={
                    r"*": {
                        "origins": os.environ.get(
                            'CORS_ORIGINS', config.CORS_ORIGINS
                        )
                    }
                }
            )

    def add_filters(self):
        self.jinja_env.filters['status_class'] = status_class
        self.jinja_env.filters['friendly_time'] = friendly_time
        self.jinja_env.filters['friendly_size'] = friendly_size
        self.jinja_env.filters['to_qs'] = to_qs
        self.jinja_env.filters['approximate_time'] = approximate_time
        self.jinja_env.filters['exact_time'] = exact_time
        self.jinja_env.filters['short_date'] = short_date


class WSGIRawBody(object):
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):

        length = environ.get('CONTENT_LENGTH', '0')
        length = 0 if length == '' else int(length)

        body = environ['wsgi.input'].read(length)
        environ['raw'] = body
        environ['wsgi.input'] = BytesIO(body)

        # Call the wrapped application
        app_iter = self.application(environ, self._sr_callback(start_response))

        # Return modified response
        return app_iter

    def _sr_callback(self, start_response):
        def callback(status, headers, exc_info=None):

            # Call upstream start_response
            start_response(status, headers, exc_info)
        return callback
