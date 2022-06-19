import tornado.web


def serve(application: tornado.web.Application, port: int) -> None:
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()