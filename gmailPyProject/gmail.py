from __future__ import print_function

import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    global msg
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # Get Messages
        results = service.users().messages().list(userId='me', labelIds=['SPAM']).execute()
        messages = results.get('messages', [])
        print("Found {} messages".format(len(messages)))
        # print("Messages type: ", type(messages), "length: ", len(messages))
        # return

        message_count = int(input("How many messages do you want to see? "))
        if not messages:
            print('No messages found.')
        else:
            print("-----------------------------------------------------------")
            print('Messages:')
            for message in messages[:message_count]:
                # print(message)
                message_id = message['id']
                # return

                msg = service.users().messages().get(userId='me', id=message_id).execute()
                ## Message keys:  dict_keys(['id', 'threadId', 'labelIds', 'snippet', 'payload', 'sizeEstimate', 'historyId', 'internalDate'])
                # print("*******Message keys: ", msg.keys())
                # #Message['payload'] keys:  dict_keys(['partId', 'mimeType', 'filename', 'headers', 'body', 'parts'])
                # print("*******Message[\'payload\'] keys: ", msg['payload'].keys())
                # print("*******Message[\'payload\'][\'headers\'] type: ", type(msg['payload']['headers']), " length: ", len(msg['payload']['headers']))
                # print("*******Message[\'payload\'][\'headers\'] 0: ", msg['payload']['headers'][0])
                # print("*******Message[\'payload\'][\'headers\'] 1: ", msg['payload']['headers'][1])
                # print("*******Message[\'payload\'][\'headers\'] 2: ", msg['payload']['headers'][2])
                print("******* Start: Message Payload Headers **************************")
                for vals in msg['payload']['headers']:
                    # print("vals", vals)
                    # print("vals[name]", vals['name'])
                    # print("vals[value]", vals['value'])

                    if vals['name'] == 'From':
                        print("## From: ", vals['value'])
                    if vals['name'] == 'Delivered-To':
                        print("## Delivered-To : ", vals['value'])
                    if vals['name'] == 'Subject':
                        print("## Subject: ", vals['value'])
                    # print(vals['name'], ": ", vals['value'])
                print("******* End: Message Payload Headers **************************")

                print("Message ID: {}".format(msg['id']))
                # print("Message ID: {}".format(message_id))
                # print(msg['snippet'])
                print("-----------------------------------------------------------")
                time.sleep(2)

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
