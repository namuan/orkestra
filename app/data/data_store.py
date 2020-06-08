import dataset

from app.signals import AppEvents, AppCommands


class DataStore:
    events: AppEvents = AppEvents()
    commands: AppCommands = AppCommands()

    def __init__(self, data_dir):
        self.data_dir = data_dir
        db_path = f"sqlite:///{self.data_dir}/orkestra.db"
        self.db = dataset.connect(db_path)

    def table_for(self, table_name):
        return self.db[table_name]
