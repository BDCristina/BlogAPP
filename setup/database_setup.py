from setup.database_updates import queries
from setup.database import init_db, get_session
from setup.database_config import DataBaseConfig


class DataBaseSetup:

    def __init__(self):
        self.credentials = DataBaseConfig()
        self.last_version = 4

    def get_session(self):
        data = self.credentials.load_credentials()
        session = get_session(data)
        return session

    def is_updated(self):
        return self.credentials.get_version() == self.last_version

    def update(self):
        session = self.get_session()
        for query in queries:
            session.execute(query)
            session.commit()
        self.credentials.update_version(self.last_version)

    def create_database(self, data):
        init_db(self.get_session(), data)
        self.credentials.get_version()
        self.update()


