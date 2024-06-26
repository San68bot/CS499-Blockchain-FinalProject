# Script used to create and issue credentials
# Second step in workflow
# Used when adding students to the class

import SecretService as sc
import requests
import time
import json

def create_credential(issuer_did,gnumber,name):
    credential = {
        "anchor": True,
        "distribute": True,
        "recipientEmail": "fadil.amiruddin@gmail.com",
        "credential": {
            "type": ["BasicCredential"],
            "name": "Sunday",
            "subject": {
                "id": gnumber,
                "FullName": name
                
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
    # TODO: Change this to the DID of the organization issuing the credential (from the DIDService.py script)
    issuer_did = "did:dock:5HcJVWWMroFctbbDE7uVz9dkm1K68ykZ7RHwcmtaydJrdivx"

    # Create the credential
    created_credential = create_credential(issuer_did)
    print("Created Credential:", json.dumps(created_credential, indent=2))

    #time.sleep(5)

    #verification_result = verify_credential(created_credential)
    #print("Verification Result:", json.dumps(verification_result, indent=2))

