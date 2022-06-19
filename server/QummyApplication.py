import tornado.web

from handler.DecryptSecretDataHandler import DecryptSecretDataHandler
from handler.GetSecretDataHandler import GetSecretDataHandler
from repo.alchemy.ServerDataRepo import ServerDataRepo


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/", RootHandler),
            (r"/api/get-secret", GetSecretDataHandler),
            (r"/api/decrypt-secret", DecryptSecretDataHandler)
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)

        self.server_data_repo = ServerDataRepo()
