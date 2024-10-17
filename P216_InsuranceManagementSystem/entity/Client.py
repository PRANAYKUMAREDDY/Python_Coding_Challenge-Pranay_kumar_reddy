
class Client:
    def __init__(self, clientId=None, clientName=None, contactInfo=None, policy=None):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policy = policy

    # Getters and Setters
    def get_clientId(self):
        return self.__clientId

    def set_clientId(self, clientId):
        self.__clientId = clientId

    def get_clientName(self):
        return self.__clientName

    def set_clientName(self, clientName):
        self.__clientName = clientName

    def get_contactInfo(self):
        return self.__contactInfo

    def set_contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    def get_policy(self):
        return self.__policy

    def set_policy(self, policy):
        self.__policy = policy

    def __str__(self):
        return f"Client [clientId={self.__clientId}, clientName={self.__clientName}, contactInfo={self.__contactInfo}, policy={self.__policy}]"