import requests
import tornado.web

from handler.ApiUrl import ApiUrl
from repo.AServerDataRepo import AServerDataRepo


class GetSecretDataHandler(tornado.web.RequestHandler):
    @property
    def sqlite_repo(self) -> AServerDataRepo:
        return self.application.server_data_repo

    def get(self):
        with requests.Session() as session:
            response = session.get(ApiUrl.top_secret_data)
            for encrypted_str in response.json():
                self.sqlite_repo.add_encrypted(encrypted_str)

            self.set_status(201)
            self.set_header("Content-Type", "application/json")
            self.write(response.text)
