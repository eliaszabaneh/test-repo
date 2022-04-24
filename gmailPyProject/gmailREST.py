import requests
import json


class ExampleOAuth2Client:
    def __init__(self, client_id, client_secret):
        self.access_token = None

        self.service = OAuth2Service(
            name="foo",
            client_id=client_id,
            client_secret=client_secret,
            access_token_url="https://oauth2.googleapis.com/token",
            authorize_url="https://accounts.google.com/o/oauth2/auth",
            base_url="http://api.example.com/",
        )

        self.get_access_token()

    def get_access_token(self):
        data = {'code': 'bar',
                'grant_type': 'client_credentials',
                'redirect_uri': 'http://example.com/'}

        session = self.service.get_auth_session(data=data, decoder=json.loads)

        self.access_token = session.access_token


api_url = 'https://www.googleapis.com/gmail/v1/users/elias.zabaneh/messages'

apisSelect = "https://www.googleapis.com/auth/gmail.readonly"
auth_code = "4%2F0AX4XfWgjnwg54hKTmSDGAJPu5782En9HSGu_3W0h3JfcyRvvy1hRYuDYtPXlKPBh80aHCQ"
access_token_field = "ya29.A0ARrdaM_3MW9JeUDh4keUKb7MHHMe-sJ_Go0lQa78qyl6oTATtsY63QuHkx_0yYY18lAIiDB8s8Ddcr9AT2ImQ1VoL2aWFthW8eE75v5UOkZg3-Mhp_fVXntCAwnqheQt7LsrmQ7n8eXkn1klDlvtRgmQ8mBG"
url = "https://gmail.googleapis.com/gmail/v1/users/elias@martinpro-me.com/messages&content_type=application/json"
url = "https://gmail.googleapis.com/gmail/v1/users/elias@martinpro-me.com/messages"
otkn = ExampleOAuth2Client(client_id='914117226377-v475mff6u4shsbhr3nnqakf5tbcbl6bk.apps.googleusercontent.com',
                           client_secret='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')
# https://developers.google.com/oauthplayground/#step3
# &apisSelect=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly
# &auth_code=4%2F0AX4XfWgjnwg54hKTmSDGAJPu5782En9HSGu_3W0h3JfcyRvvy1hRYuDYtPXlKPBh80aHCQ
# &access_token_field=ya29.A0ARrdaM_3MW9JeUDh4keUKb7MHHMe-sJ_Go0lQa78qyl6oTATtsY63QuHkx_0yYY18lAIiDB8s8Ddcr9AT2ImQ1VoL2aWFthW8eE75v5UOkZg3-Mhp_fVXntCAwnqheQt7LsrmQ7n8eXkn1klDlvtRgmQ8mBG
# &url=https%3A%2F%2Fgmail.googleapis.com%2Fgmail%2Fv1%2Fusers%2Felias%40martinpro-me.com%2Fmessages
# &content_type=application%2Fjson
# &http_method=GET
# &useDefaultOauthCred=unchecked
# &oauthEndpointSelect=Google
# &oauthAuthEndpointValue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fv2%2Fauth
# &oauthTokenEndpointValue=https%3A%2F%2Foauth2.googleapis.com%2Ftoken
# &expires_in=3599
# &access_token_issue_date=1649751775
# &for_access_token=ya29.A0ARrdaM_3MW9JeUDh4keUKb7MHHMe-sJ_Go0lQa78qyl6oTATtsY63QuHkx_0yYY18lAIiDB8s8Ddcr9AT2ImQ1VoL2aWFthW8eE75v5UOkZg3-Mhp_fVXntCAwnqheQt7LsrmQ7n8eXkn1klDlvtRgmQ8mBG
# &includeCredentials=checked
# &accessTokenType=query&autoRefreshToken=unchecked
# &accessType=offline&prompt=consent&response_type=token&wrapLines=on
