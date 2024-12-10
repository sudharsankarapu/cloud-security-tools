from google.cloud import storage

# Initialize GCP storage client
client = storage.Client()

print("Scanning GCP buckets for public access...")

# List all buckets
buckets = client.list_buckets()
for bucket in buckets:
    iam_policy = bucket.get_iam_policy()
    for role in iam_policy:
        if "allUsers" in iam_policy[role] or "allAuthenticatedUsers" in iam_policy[role]:
            print(f"Bucket {bucket.name} is publicly accessible!")
