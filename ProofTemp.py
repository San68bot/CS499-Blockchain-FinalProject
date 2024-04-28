import SecretService as sc
import requests
import time
import json

def create_proof_request_template(proof_request_data):
    # Endpoint to create a proof request template
    url = f"{sc.BASE_URL}/proof-templates"

    # Send the POST request
    response = requests.post(url, headers=sc.headers, json=proof_request_data)

    # Check for a successful response and return JSON, or raise an exception
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to create proof request template: {response.text}")

# Example data for creating a proof request template
proof_request_data = {
    "name": "b",
    "issuer": "did:dock:5FDnJYH8c6adynWjhZE4N4kRjcqRVZCWfYHz22WAbuKsYNPY", # TODO: Change this to the DID of the organization issuing the credential (from the DIDService.py script)
}

# Create the proof request template
try:
    result = create_proof_request_template(proof_request_data)
    print("Proof Request Template Created:", json.dumps(result, indent=2))
except Exception as e:
    print(str(e))