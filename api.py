import  jsonify
import subprocess


command = '''
    API_KEY="eyJzY29wZXMiOlsidGVzdCIsImFsbCJdLCJzdWIiOiIxNjAxMyIsInNlbGVjdGVkVGVhbUlkIjoiMTk5NDkiLCJjcmVhdG9ySWQiOiIxNjAxMyIsImlhdCI6MTcxNDg5MDE2MywiZXhwIjo0Nzk0MTg2MTYzfQ.d8cvwvqvqWcvO1vBddoegD9uFXwVp3DdSNX9A4YAFD74dlDVEpy_PFdALZKjn-HXgdsCrfRZm95ftrn1U57pEw"

    curl 'https://api-testnet.dock.io/proof-templates/d0155104-c2d0-4fe2-b5e8-f79ddb570047/history?offset=0&limit=64' \
      -H 'accept: application/json' \
      -H "DOCK-API-TOKEN: $API_KEY" | jq -r '.[] | .presentation.credentials[].name'
    '''

    # Execute the command
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print(result.stdout)

