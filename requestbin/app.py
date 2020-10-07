from requestbin import MyApplication
import requestbin.views as views
import requestbin.api as api


app = MyApplication(__name__)

app.add_url_rule('/', 'views.home', views.home)
views.bin.methods = [
    'GET',
    'POST',
    'DELETE',
    'PUT',
    'OPTIONS',
    'HEAD',
    'PATCH',
    'TRACE'
]
app.add_url_rule('/<path:name>', 'views.bin', views.bin)
app.add_url_rule('/docs/<name>', 'views.docs', views.docs)

api.bins.provide_automatic_options = False
api.bins.methods = ['POST']
app.add_url_rule(
    '/api/v1/bins', 'api.bins', api.bins)

api.bin.provide_automatic_options = False
api.bin.methods = ['GET']
app.add_url_rule(
    '/api/v1/bins/<name>', 'api.bin', api.bin)

api.requests.provide_automatic_options = False
api.requests.methods = ['GET']
app.add_url_rule('/api/v1/bins/<bin>/requests',
                 'api.requests', api.requests, methods=['GET'])


api.request_.provide_automatic_options = False
api.request_.methods = ['GET']
app.add_url_rule('/api/v1/bins/<bin>/requests/<name>', 'api.request_', api.request_)


app.add_url_rule('/api/v1/stats', 'api.stats', api.stats)
