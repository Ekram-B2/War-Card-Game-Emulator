from sqlalchemy import create_engine
from models.models import base
from sqlalchemy.orm import sessionmaker
from models.transactionmanager import TransactionManager
from sqlalchemy.exc import SQLAlchemyError

class SessionManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        base.metadata.create_all(self.engine)
    
    def execute_tranaction(self, transaction_manager, rest_client, http_method, data={}):
        if http_method == "get":
            observations = transaction_manager.read(self.session, rest_client)
            return observations
        elif http_method == "post":
            transaction_manager.insert(self.session, rest_client, data)
            return []

session_manager = SessionManager("sqlite:////root/sqlite.db")
session_manager.create_tables()