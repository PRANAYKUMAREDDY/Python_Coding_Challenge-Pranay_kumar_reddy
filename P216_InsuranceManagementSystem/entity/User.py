class User:
    def __init__(self, userId=None, username=None, password=None, role=None):
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    # Getters and Setters
    def get_userId(self):
        return self.__userId

    def set_userId(self, userId):
        self.__userId = userId

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role


    def __str__(self):
        return f"User [userId={self.__userId}, username={self.__username}, role={self.__role}]"