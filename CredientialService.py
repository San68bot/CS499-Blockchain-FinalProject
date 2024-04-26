# Script used to create and issue credentials
# Second step in workflow
# Used when adding students to the class

import SecretService as sc
import requests
import time
import json

def create_credential(issuer_did):
    credential = {
        "persist": True,
        "password": "q123",
        "credential": {
            "type": ["BasicCredential"],
            "name": "testing",
            "subject": {
                "id": "G1234567890",
                "name": "John Doe"
            },
            "issuer": issuer_did
        }
    }

    # Make the POST request to create the credential
    response = requests.post(f"{sc.BASE_URL}/credentials", headers=sc.headers, json=credential)
    return response.json()


def verify_credential(credential):
    response = requests.post(f"{sc.BASE_URL}/verify/", headers=sc.headers, json=credential)
    return response.json()

if __name__ == "__main__":
    issuer_did = "did:dock:5FDnJYH8c6adynWjhZE4N4kRjcqRVZCWfYHz22WAbuKsYNPY"

    # Create the credential
    created_credential = create_credential(issuer_did)
    print("Created Credential:", json.dumps(created_credential, indent=2))

    time.sleep(5)

    verification_result = verify_credential(created_credential)
    print("Verification Result:", json.dumps(verification_result, indent=2))


