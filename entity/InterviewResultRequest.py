from typing import List

from pydantic import BaseModel, AnyHttpUrl


class InterviewResultRequest(BaseModel):
    name: str
    repo_url: AnyHttpUrl
    result: List[str]