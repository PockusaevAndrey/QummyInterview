import json

import requests
import tornado.web
from tornado.escape import json_decode

from config import RemoteServerConfig
from entity.InterviewResultRequest import InterviewResultRequest
from handler.ApiUrl import ApiUrl
from repo.AServerDataRepo import AServerDataRepo


class SendInterviewResultHandler(tornado.web.RequestHandler):
    @property
    def sqlite_repo(self) -> AServerDataRepo:
        return self.application.server_data_repo

    def post(self):
        request = InterviewResultRequest(**json_decode(self.request.body))
        with requests.Session() as session:
            session.auth = RemoteServerConfig.credentials
            response = session.post(ApiUrl.result, json=request.dict())
            self.write(json.dumps({"status": "Success"}))