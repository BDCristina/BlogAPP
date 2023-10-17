from setup.config import Config
from models.database_credentials import DataBaseCredentials


class DataBaseConfig(Config):

    def __init__(self):
        self.section = 'postgresql'
        super().__init__()

    def get_version(self):
        data = super().load(self.section)
        if 'version' not in data:
            super().update(self.section, 'version', '1')
            data_updated = super().load(self.section)
            return int(data_updated['version'])
        return int(data['version'])

    def update_version(self, updated_version):
        super().update(self.section, 'version', updated_version)

    def load_credentials(self):
        data = super().load()
        database_credentials = DataBaseCredentials(data['user'],
                                                   data['password'],
                                                   data['database'])
        return database_credentials

    def save_credentials(self, data_setup: DataBaseCredentials):
        credentials = {
            "host" : data_setup.host,
            "user" : data_setup.user,
            "password" : data_setup.password,
            "database" : data_setup.database_name
        }
        super().save(self.section, credentials)