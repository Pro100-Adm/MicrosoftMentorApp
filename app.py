def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    response_body = '<input></input><button>Get!</button>'
    yield response_body.encode()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
