# Script to create an Organization DID
# First step in workflow
# Used when creating class for example

import SecretService as sc
import requests
import time

def create_did():
    """Create a new DID."""
    json_data = {
        'type': 'dock',
        'keyType': 'sr25519',
    }

    response = requests.post(
        f'{sc.BASE_URL}/dids',
        json=json_data, headers=sc.headers
    )

    return response.json()

def get_did(did_id):
    """Retrieve a DID by its identifier."""
    response = requests.get(f'{sc.BASE_URL}/dids/{did_id}', headers=sc.headers)
    return response.json()

def list_dids():
    """List all DIDs."""
    response = requests.get(f'{sc.BASE_URL}/dids', headers=sc.headers)
    return response.json()

def update_did(did_id, body):
    """Update an existing DID."""
    response = requests.patch(f'{sc.BASE_URL}/dids/{did_id}', json=body, headers=sc.headers)
    return response.json()

def delete_did(did_id):
    """Delete a DID."""
    response = requests.delete(f'{sc.BASE_URL}/dids/{did_id}', headers=sc.headers)
    return response.json()

if __name__ == "__main__":
    # Create a DID
    did_creation_response = create_did()
    print("Create DID:", did_creation_response)

    if 'id' in did_creation_response:
        time.sleep(5)
        did_info = get_did(did_creation_response['did'])
        print("Retrieved DID:", did_info)

        # Save the DID creation response to a text file
        with open('generated_did.txt', 'w') as file:
            file.write(str(did_creation_response))
            file.write('\n')
            file.write(str(did_info))
    else:
        print("Failed to retrieve the DID ID from the creation response.")

