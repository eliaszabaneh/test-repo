import requests

api_url = 'https://www.googleapis.com/gmail/v1/users/elias.zabaneh/messages'

apisSelect = "https://www.googleapis.com/auth/gmail.readonly"
auth_code = "4%2F0AX4XfWgjnwg54hKTmSDGAJPu5782En9HSGu_3W0h3JfcyRvvy1hRYuDYtPXlKPBh80aHCQ"
access_token_field = "ya29.A0ARrdaM_3MW9JeUDh4keUKb7MHHMe-sJ_Go0lQa78qyl6oTATtsY63QuHkx_0yYY18lAIiDB8s8Ddcr9AT2ImQ1VoL2aWFthW8eE75v5UOkZg3-Mhp_fVXntCAwnqheQt7LsrmQ7n8eXkn1klDlvtRgmQ8mBG"
url = "https://gmail.googleapis.com/gmail/v1/users/elias@martinpro-me.com/messages"


def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        # data={"auth_uri", "token_uri", "client_id", "client_secret"},
        data={'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': url, 'client_id': client_id,
              'client_secret': client_secret},
        auth=(client_id, client_secret))
    print(response.json())
    return response.json()  # ["access_token"]


get_access_token("https://oauth2.googleapis.com/token",
                 "914117226377-v475mff6u4shsbhr3nnqakf5tbcbl6bk.apps.googleusercontent.com",
                 "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")
