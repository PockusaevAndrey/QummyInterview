from datetime import datetime

from pydantic import BaseModel


class ServerData(BaseModel):
    id: int
    encrypted_text: str
    decrypted_text: str
    created_at: datetime

    class Config:
        orm_mode = True

