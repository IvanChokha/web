def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    res = ["\n".join(environ.get('QUERY_STRING').split("&")).encode('utf-8')]
    return res
