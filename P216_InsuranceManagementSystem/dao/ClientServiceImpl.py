# dao/ClientServiceImpl.py
import pyodbc
from entity.Client import Client
from util.DBConnUtil import DBConnUtil

class ClientServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def createClient(self, client):
        cursor = self.conn.cursor()
        query = "INSERT INTO Clients (clientName, contactInfo, policy) VALUES (?, ?, ?)"
        cursor.execute(query, client.get_clientName(), client.get_contactInfo(), client.get_policy())
        self.conn.commit()
        return True

    def getClient(self, clientId):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Clients WHERE clientId = ?"
        cursor.execute(query, clientId)
        result = cursor.fetchone()
        if result:
            return Client(clientId=result.clientId, clientName=result.clientName, contactInfo=result.contactInfo, policy=result.policy)
        else:
            return None

    def getAllClients(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Clients"
        cursor.execute(query)
        clients = []
        for row in cursor.fetchall():
            client = Client(clientId=row.clientId, clientName=row.clientName, contactInfo=row.contactInfo, policy=row.policy)
            clients.append(client)
        return clients

    def updateClient(self, client):
        cursor = self.conn.cursor()
        query = "UPDATE Clients SET clientName = ?, contactInfo = ?, policy = ? WHERE clientId = ?"
        cursor.execute(query, client.get_clientName(), client.get_contactInfo(), client.get_policy(), client.get_clientId())
        self.conn.commit()
        return True

    def deleteClient(self, clientId):
        cursor = self.conn.cursor()
        query = "DELETE FROM Clients WHERE clientId = ?"
        cursor.execute(query, clientId)
        self.conn.commit()
        return True