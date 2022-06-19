from sqlalchemy import insert, update
from sqlalchemy.orm import Session

from db import ServerTable, engine
from repo.AServerDataRepo import AServerDataRepo


class ServerDataRepo(AServerDataRepo):
    def add_encrypted(self, encrypted_text: str) -> None:
        with Session(engine) as session:
            session.execute(insert(ServerTable).values((None, encrypted_text, None)))
            session.commit()

    def add_decrypted(self, encrypted_text: str, decrypted_text: str) -> None:
        with Session(engine) as session:
            session.execute(update(ServerTable)
                            .where(ServerTable.encrypted_text == encrypted_text)
                            .values(decrypted_text=decrypted_text))

            session.commit()
