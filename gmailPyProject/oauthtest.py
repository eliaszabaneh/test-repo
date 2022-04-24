import sys
import requests
import json
import logging
import time

logging.captureWarnings(True)

test_api_url = "https://www.googleapis.com/gmail/v1/users/elias@martinpro-me.com/messages"


##
##    function to obtain a new OAuth 2.0 token from the authentication server
##
def get_new_token():
    auth_server_url = "https://accounts.google.com/o/oauth2/auth"
    client_id = "914117226377-v475mff6u4shsbhr3nnqakf5tbcbl6bk.apps.googleusercontent.com"
    client_secret = "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"

    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_server_url, data=token_req_payload, verify=False, allow_redirects=False,
                                   auth=(client_id, client_secret))

    if token_response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server *** ", token_response.status_code, " *** " , file=sys.stderr)
        sys.exit(1)

        print("Successfuly obtained a new token")
        tokens = json.loads(token_response.text)
        return tokens['access_token']

    ##
    ## 	obtain a token before calling the API for the first time
    ## 	the token is valid for 15 minutes
    ##
    token = get_new_token()

    while True:
        ##
        ##   call the API with the token
        ##
        api_call_headers = {'Authorization': 'Bearer ' + token}
        api_call_response = requests.get(test_api_url, headers=api_call_headers)  # (verify + False))

        ##
        ##
        if api_call_response.status_code == 401:
            token = get_new_token()
        else:
            print(api_call_response.text)

        time.sleep(30)


if __name__ == '__main__':
    get_new_token()
