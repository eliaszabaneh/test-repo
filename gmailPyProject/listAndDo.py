from __future__ import print_function

import os.path
import time
import csv

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
                'credez.json', SCOPES)
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
        f = None
        message_count = int(input("How many messages do you want to see? "))
        if not messages:
            print('No messages found.')
        else:
            print("-----------------------------------------------------------")
            print('Messages:')
            iter = 0
            for message in messages[:message_count]:
                # print(message)
                # return
                iter = iter + 1
                message_id = message['id']
                msg = service.users().messages().get(userId='me', id=message_id).execute()

                print("******* Start: Message Payload Headers ({})**************************".format(iter))
                # format CSV record
                try:
                    f = open("spam_messages.csv", "a")
                except IOError:
                    print("Could not open file")
                    return
                else:
                    # write header
                    if os.stat("spam_messages.csv").st_size == 0:
                        f.write("Message ID, From, Date\n")
                    messageID = message['id']
                    # print(msg['payload']['headers'])
                    # return
                    for vals in msg['payload']['headers']:
                        if vals['name'] == 'From':
                            try:
                                cleanfrom = vals['value'].split('<')[1].split('>')[0]
                                messageFrom = cleanfrom
                            except IndexError:
                                print(vals['value'] + " is not a valid email address")
                            # print("From: ", cleanfrom)
                            # print("## From: ", vals['value'])
                        if vals['name'] == 'Date':
                            messageDate = vals['value']
                    if len(messageDate.split(',')) > 1:
                        messageDate = messageDate.split(',')[1].strip()
                    # print("{0}, {1}, {2}\n".format(message['id'], messageFrom, messageDate.split(',')[1]))
                    print("{0}, {1}, {2}\n".format(message['id'], messageFrom, messageDate))
                    # return
                    # f.write("{0}, {1}, {2}\n".format(message['id'], messageFrom, messageDate.split(',')[1]))  ## , msg['snippet'], msg['payload']['headers'], msg['payload']['headers'][0], msg['payload']['headers'][1], msg['payload']['headers'][2], msg['sizeEstimate'], msg['historyId'], msg['internalDate']))
            if f is not None:
                f.close()
            return
            print("******* End: Message Payload Headers **************************")
            # time.sleep(2)

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()
