import sqlite3
from sqlite3 import Error
from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    @abstractmethod
    def test_connection(self):
        pass

class SqlLiteClient(Client):
    def __init__(self, connection_string):
        self.connection_string = connection_string
   
    def test_connection(self):
        """
        :rtype is_success : boolean
        """
        # 1. Try establishing a connection
        conn = None
        is_success = False
        try:
            conn = sqlite3.connect(self.connection_string)
            is_success = True
        except Error as e:
            print("SYSTEM-ERROR: unable to connect to database: {}".format(e))
            is_success = False
        finally:
            # 2. Regardless of success or failure, close the connection if its still active
            if conn:
                conn.close()
            return is_success

    def __str__(self):
        return "SQLite Client"
        
def get_database_client(clientType, connection_string):
    # 1. return a run time client based on the type
    if clientType == "sqlite":
        return SqlLiteClient(connection_string)
    else:
        # currently only one client exits
        return SqlLiteClient(connection_string)