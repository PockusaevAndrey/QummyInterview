from sqlalchemy import create_engine, MetaData

engine = create_engine(r"sqlite:///sqlite.db", echo=True)
