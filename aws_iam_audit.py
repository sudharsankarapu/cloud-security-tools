import boto3

# Create an IAM client
iam = boto3.client('iam')

# Fetch all IAM users
users = iam.list_users()['Users']

print("Checking IAM user permissions...")

# Iterate through users
for user in users:
    username = user['UserName']
    policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
    if not policies:
        print(f"User {username} has no attached policies.")
    else:
        print(f"User {username} has the following policies:")
        for policy in policies:
            print(f"- {policy['PolicyName']}")
