# dao/PolicyServiceImpl.py
import pyodbc
from dao.IPolicyService import IPolicyService
from entity.Policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException
from util.DBConnUtil import DBConnUtil

class PolicyServiceImpl(IPolicyService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def createPolicy(self, policy):
        cursor = self.conn.cursor()
        query = "INSERT INTO Policies (policyName, policyDescription) VALUES (?, ?)"
        cursor.execute(query, policy.get_policyName(), policy.get_policyDescription())
        self.conn.commit()
        return True

    def getPolicy(self, policyId):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Policies WHERE policyId = ?"
        cursor.execute(query, policyId)
        result = cursor.fetchone()
        if result:
            return Policy(policyId=result.policyId, policyName=result.policyName, policyDescription=result.policyDescription)
        else:
            raise PolicyNotFoundException(f"Policy with ID {policyId} not found.")

    def getAllPolicies(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Policies"
        cursor.execute(query)
        policies = []
        for row in cursor.fetchall():
            policy = Policy(policyId=row.policyId, policyName=row.policyName, policyDescription=row.policyDescription)
            policies.append(policy)
        return policies

    def updatePolicy(self, policy):
        cursor = self.conn.cursor()
        query = "UPDATE Policies SET policyName = ?, policyDescription = ? WHERE policyId = ?"
        cursor.execute(query, policy.get_policyName(), policy.get_policyDescription(), policy.get_policyId())
        self.conn.commit()
        return True

    def deletePolicy(self, policyId):
        cursor = self.conn.cursor()
        query = "DELETE FROM Policies WHERE policyId = ?"
        cursor.execute(query, policyId)
        self.conn.commit()
        return True