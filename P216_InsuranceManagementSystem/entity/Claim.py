# entity/Claim.py
class Claim:
    def __init__(self, claimId=None, claimNumber=None, dateFiled=None, claimAmount=None, status=None, policy=None, client=None):
        self.__claimId = claimId
        self.__claimNumber = claimNumber
        self.__dateFiled = dateFiled
        self.__claimAmount = claimAmount
        self.__status = status
        self.__policy = policy
        self.__client = client

    # Getters and Setters
    def get_claimId(self):
        return self.__claimId

    def set_claimId(self, claimId):
        self.__claimId = claimId

    def get_claimNumber(self):
        return self.__claimNumber

    def set_claimNumber(self, claimNumber):
        self.__claimNumber = claimNumber

    def get_dateFiled(self):
        return self.__dateFiled

    def set_dateFiled(self, dateFiled):
        self.__dateFiled = dateFiled

    def get_claimAmount(self):
        return self.__claimAmount

    def set_claimAmount(self, claimAmount):
        self.__claimAmount = claimAmount

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_policy(self):
        return self.__policy

    def set_policy(self, policy):
        self.__policy = policy

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    # String representation
    def __str__(self):
        return (f"Claim [claimId={self.__claimId}, claimNumber={self.__claimNumber}, dateFiled={self.__dateFiled}, "
                f"claimAmount={self.__claimAmount}, status={self.__status}, policy={self.__policy}, client={self.__client}]")