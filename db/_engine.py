from sqlalchemy import create_engine, MetaData

from config import SQLiteConfig

engine = create_engine(SQLiteConfig.path, echo=True)
