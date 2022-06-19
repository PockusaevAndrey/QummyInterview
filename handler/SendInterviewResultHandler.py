import requests
import tornado.web
from tornado.escape import json_decode

from entity.InterviewResultRequest import InterviewResultRequest
from repo.AServerDataRepo import AServerDataRepo


class SendInterviewResultHandler(tornado.web.RequestHandler):
    @property
    def sqlite_repo(self) -> AServerDataRepo:
        return self.application.server_data_repo

    def post(self):
        request = InterviewResultRequest(**json_decode(self.request.body))
        with requests.Session() as session:
            session.auth = ("qummy", "GiVEmYsecReT!")
            response = session.post("http://yarlikvid.ru:9999/api/decrypt", json=request.dict())
