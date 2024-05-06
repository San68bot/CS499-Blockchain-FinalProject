from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/get_credentials', methods=['GET'])
def get_credentials():
    # Command to execute
    command = '''
    API_KEY="eyJzY29wZXMiOlsidGVzdCIsImFsbCJdLCJzdWIiOiIxNjAxMyIsInNlbGVjdGVkVGVhbUlkIjoiMTk5NDkiLCJjcmVhdG9ySWQiOiIxNjAxMyIsImlhdCI6MTcxNDg5MDE2MywiZXhwIjo0Nzk0MTg2MTYzfQ.d8cvwvqvqWcvO1vBddoegD9uFXwVp3DdSNX9A4YAFD74dlDVEpy_PFdALZKjn-HXgdsCrfRZm95ftrn1U57pEw"

    curl 'https://api-testnet.dock.io/proof-templates/d0155104-c2d0-4fe2-b5e8-f79ddb570047/history?offset=0&limit=64' \
      -H 'accept: application/json' \
      -H "DOCK-API-TOKEN: $API_KEY" | jq -r '.[] | .presentation.credentials[].name'
    '''

    # Execute the command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        # If the command executed successfully, return the output
        return jsonify({"credentials": result.stdout.splitlines()})
    else:
        # If there was an error executing the command, return an error message
        return jsonify({"error": "Failed to retrieve credentials"}), 500

if __name__ == '__main__':
    app.run(debug=True)
