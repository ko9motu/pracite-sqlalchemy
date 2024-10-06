from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///user.db"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self, base):
        base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()
