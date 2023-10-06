import mysql.connector


class DatabaseConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def fetch_as_list(cursor):
        return [list(row) for row in cursor.fetchall()]
    
    def fetch_as_dict(cursor):
        columns = cursor.column_names
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

config = {}

