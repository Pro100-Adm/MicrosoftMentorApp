from cgi import parse_qs
import test
html = '<form method="get"><input name="ip"></input><button>Get!</button></form>'
def wsgi_app(environ, start_response):
    status = '200 OK'
    d = parse_qs(environ['QUERY_STRING'])
    ip = d.get('ip',[None])[0]
    x = []
    x.append(ip)
    response_headers = [('Content-type', 'text/html')]
    response_body = html
    if ip:
        response_headers = [('Content-type', 'text/html')]
        if test.ip_check_Azure(x[0]):
            response_body = test.ip_check_Azure(x[0])
        elif test.ip_check_Amazon(x[0]):
            response_body = test.ip_check_Amazon(x[0])
        else:
            response_body = 'Not Found!'
    else:
        response_headers = [('Content-type', 'text/html')]
        response_body = html
    start_response(status, response_headers)
    yield response_body.encode()
    

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
