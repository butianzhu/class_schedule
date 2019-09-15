def application(environ, start_response):
    """
    http处理函数
    :param environ: 一个包含所有HTTP请求信息的dict对象
    :param start_response: 一个发送HTTP响应的函数
    :return:
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]