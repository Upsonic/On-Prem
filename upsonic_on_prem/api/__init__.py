from .urls import *






from waitress import serve
from flask import Flask, request, Response, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


from werkzeug.middleware.proxy_fix import ProxyFix

from upsonic_on_prem.api.utils.configs import *

if sentry:
    import sentry_sdk

    sentry_sdk.init(
        dsn=sentry_flask_key,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )

app = Flask(__name__)

from upsonic_on_prem.api.utils import storage

database_name_caches = []
key_name_caches = []



app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
limiter = Limiter(get_remote_address, app=app, default_limits=rate_limit)


from .tracer import provider
from opentelemetry.instrumentation.flask import FlaskInstrumentor

FlaskInstrumentor().instrument_app(app, tracer_provider=provider)





@app.route(status_url, methods=["GET"])
def status():
    return jsonify({"status": True, "result": True})




def version_info():
    from upsonic_on_prem.api.utils.logs import successfully
    from upsonic_on_prem.__init__ import __version__
    successfully(f"Upsonic On-Prem Alive with version {str(__version__)}")


version_info()



from .limit import *
from .pre_process import *

from .operations import *


