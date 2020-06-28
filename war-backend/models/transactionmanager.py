from models.restclient import RestClient

class TransactionManager:
    def __init__(self):
        pass

    def read(self, session, restClient):
        """
        :type session : session object
        :type RestClient : RestClient 
        :rtype observations: List[sqlalchemy.object]
        """
        # 1. Apply read operation
        observations = restClient.get_from_store(session)
        # 2. return the observations
        return observations

    def insert(self, session, restClient, data):
        # 1. Apply the write opereation
        restClient.insert_in_store(data, session)
        # 2. Close session object
        session.close()

