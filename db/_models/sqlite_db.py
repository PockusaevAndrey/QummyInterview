import sqlalchemy
from sqlalchemy.sql import func

from db._models import Base


class ServerTable(Base):
    __tablename__ = 'server_data'
    __tableargs__ = {'autoload': True}
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    encrypted_text = sqlalchemy.Column(sqlalchemy.String())
    decrypted_text = sqlalchemy.Column(sqlalchemy.String())
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
