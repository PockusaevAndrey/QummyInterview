from db._engine import engine
from db._models import Base
from db._models.sqlite_db import ServerTable

Base.metadata.create_all(engine)
