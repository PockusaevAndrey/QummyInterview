import tornado.web

from handler.DecryptSecretDataHandler import DecryptSecretDataHandler
from handler.GetSecretDataHandler import GetSecretDataHandler
from handler.SendInterviewResultHandler import SendInterviewResultHandler
from repo.alchemy.ServerDataRepo import ServerDataRepo


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/api/get-secret", GetSecretDataHandler),
            (r"/api/decrypt-secret", DecryptSecretDataHandler),
            (r"/api/send-result", SendInterviewResultHandler)
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)

        self.server_data_repo = ServerDataRepo()
