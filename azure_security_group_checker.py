from azure.identity import AzureCliCredential
from azure.mgmt.network import NetworkManagementClient

# Authenticate using Azure CLI
credential = AzureCliCredential()
subscription_id = "<YOUR_SUBSCRIPTION_ID>"
network_client = NetworkManagementClient(credential, subscription_id)

print("Checking security groups...")

# Fetch all security groups
security_groups = network_client.network_security_groups.list_all()
for sg in security_groups:
    print(f"Security Group: {sg.name}")
    for rule in sg.security_rules:
        if rule.access == "Allow" and rule.destination_port_range == "*":
            print(f"  Insecure rule: {rule.name} allows all traffic!")
