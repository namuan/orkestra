import dataset


class DataStore:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        db_path = f"sqlite:///{self.data_dir}/orkestra.db"
        self.db = dataset.connect(db_path)

    def table_for(self, table_name):
        return self.db[table_name]
