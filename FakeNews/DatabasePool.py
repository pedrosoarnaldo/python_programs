import mysql.connector

class DatabasePool():
    """Class created to optmize connection with database"""

    def __init__(self, host_name="localhost", database_name="fakenews", user_name="root", password="Zse4nji9123!@#"):
        self.host_name = host_name
        self.database_name = database_name
        self.user_name = user_name
        self.password = password

    def open_connection(self):
        return mysql.connector.connect(user=self.user_name, password=self.password,
                                       host=self.host_name, database=self.database_name)
