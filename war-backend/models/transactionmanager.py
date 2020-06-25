from models.transactionmanager import RestClient

class TransactionManager:

    def read(self, RestClient):
        """
        :type RestClient : RestClient 
        :rtype observations: List[sqlalchemy.object]
        """
        # 1. Create a new session object
        new_session = self.session()
        # 2. Apply read operation
        observations = RestClient.get_from_store()
        # 3. Close the session
        new_session.close()
        # 4. return the observations
        return observations

    def insert(self, RestClient, data):
        # 1. Create a new session object
        new_session = self.session()
        # 2. Apply the write opereation
        RestClient.insert_in_store(data)
        # 3. Close session object
        new_session.close()
