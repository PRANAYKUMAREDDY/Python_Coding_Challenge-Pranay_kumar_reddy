from dao.PolicyServiceImpl import PolicyServiceImpl
from dao.ClientServiceImpl import ClientServiceImpl
from entity.Policy import Policy
from entity.Client import Client
from entity.Claim import Claim
from entity.User import User
from entity.Payment import Payment
from exception.PolicyNotFoundException import PolicyNotFoundException

if __name__ == "__main__":
    # Create instances of service classes
    policy_service = PolicyServiceImpl()
    client_service = ClientServiceImpl()


    while True:
        print("\nInsurance Management System")
        print("1. Create Client")
        print("2. Create Policy")
        print("3. Get Policy")
        print("4. Get All Policies")
        print("5. Update Policy")
        print("6. Delete Policy")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Create Client
            clientName = input("Enter client name: ")
            contactInfo = input("Enter contact info: ")
            policy = input("Enter policy: ")
            client = Client(clientName=clientName, contactInfo=contactInfo, policy=policy)
            client_service.createClient(client)
            print("Client created successfully!")

        elif choice == '2':  # Create Policy
            policyName = input("Enter policy name: ")
            policyDescription = input("Enter policy description: ")
            policy = Policy(policyName=policyName, policyDescription=policyDescription)
            policy_service.createPolicy(policy)
            print("Policy created successfully!")

        elif choice == '3':  # Get Policy
            policyId = int(input("Enter policy ID: "))
            try:
                policy = policy_service.getPolicy(policyId)
                print(policy)
            except PolicyNotFoundException as e:
                print(e)

        elif choice == '4':  # Get All Policies
            policies = policy_service.getAllPolicies()
            for policy in policies:
                print(policy)

        elif choice == '5':  # Update Policy
            policyId = int(input("Enter policy ID: "))
            policyName = input("Enter new policy name: ")
            policyDescription = input("Enter new policy description: ")
            policy = Policy(policyId=policyId, policyName=policyName, policyDescription=policyDescription)
            policy_service.updatePolicy(policy)
            print("Policy updated successfully!")

        elif choice == '6':  # Delete Policy
            policyId = int(input("Enter policy ID: "))
            policy_service.deletePolicy(policyId)
            print("Policy deleted successfully!")


        elif choice == '7':  # Exit
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")