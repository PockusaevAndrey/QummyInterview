from typing import Iterable


class SQLiteConfig:
    path = "sqlite:///sqlite.db"


class RemoteServerConfig:
    host = "http://yarlikvid.ru:9999"
    credentials = ("qummy", "GiVEmYsecReT!")
