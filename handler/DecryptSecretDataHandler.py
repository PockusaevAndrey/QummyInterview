from requests import Session
import tornado.web
from tornado.escape import json_decode

from config import RemoteServerConfig
from handler.ApiUrl import ApiUrl
from repo.AServerDataRepo import AServerDataRepo


class DecryptSecretDataHandler(tornado.web.RequestHandler):
    @property
    def sqlite_repo(self) -> AServerDataRepo:
        return self.application.server_data_repo

    def post(self):
        request = json_decode(self.request.body)

        with Session() as session:
            session.auth = RemoteServerConfig.credentials
            response = session.post(ApiUrl.decrypt, json=request)

            for encrypted, decrypted in zip(request, response.json()):
                self.sqlite_repo.add_decrypted(encrypted, decrypted)

            self.set_status(201)
            self.set_header('Content-Type', 'application/json')
            self.write(response.text)



