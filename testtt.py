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
    
# Create the proof request from the template
try:
    result = create_proof_request_from_template("d0155104-c2d0-4fe2-b5e8-f79ddb570047")
    print("Proof Request Created:", json.dumps(result, indent=2))
    import time

    # Countdown for 30 seconds
    for i in range(45, 0, -1):
        print(f"Waiting: {i} seconds remaining", end='\r')
        time.sleep(1)
    print("Continuing with the process...")

    print("Proof Request Created:", result['verified'])
except Exception as e:
    print(str(e))