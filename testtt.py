import json

import requests
import SecretService as sc

def create_proof_request_from_template(template_id):
    # Endpoint to create a proof request from a template
    url = f"{sc.BASE_URL}/proof-templates/{template_id}/request"

    # Send the POST request
    response = requests.post(url, headers=sc.headers)

    # Check for a successful response and return JSON, or raise an exception
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to create proof request from template: {response.status_code} {response.text}")

def get_proof_request(proof_request_id):
    # Endpoint to get a proof request
    url = f"{sc.BASE_URL}/proof-requests/{proof_request_id}"

    # Send the GET request
    response = requests.get(url, headers=sc.headers)

    # Check for a successful response and return JSON, or raise an exception
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve proof request: {response.status_code} {response.text}")

def get_proof_template_history(id):
    # Endpoint to get a proof request
    url = f"{sc.BASE_URL}/proof-templates/{id}/history"

    # Send the GET request
    response = requests.get(url, headers=sc.headers)

    # Check for a successful response and return JSON, or raise an exception
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve proof request: {response.status_code} {response.text}")


template_id = 'd8980f04-8779-4b24-a75f-fb1b6903888e'
proof_request_id = 'd191f12b-c874-4f59-856d-41f5167ba9c5'

# Create the proof request from the template
try:
    result = create_proof_request_from_template(template_id)
    print("Proof Request Created:", json.dumps(result, indent=2))
    print("Proof Request Created:", result[0]['verified'])
except Exception as e:
    print(str(e))