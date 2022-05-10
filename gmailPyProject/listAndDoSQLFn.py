from __future__ import print_function

import os.path
import time
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify',
          'https://mail.google.com/']


def insertMessageDB(message_id, messageFrom, messageDate, service):
    # insert message into database
    cur.execute("SELECT * FROM spam WHERE msgID = ?", (message_id,))
    if cur.fetchone():
        print("Message already exists in database")
        return
    else:
        print("Message not in database")
        # insert message into database
        cur.execute(
            # "INSERT INTO spam (msgID, msgFrom, msgDate, msgSeen, msgDeleted, msgNotes) VALUES (?,?,?,?,?,?)",
            "INSERT INTO spam (msgID, msgFrom, msgDate) VALUES (?,?,?)",
            (message_id, messageFrom, messageDate))
        con.commit()
        print("Message inserted into database")
    pass


def deleteMessage(message_id, service, cur, con):
    try:
        # delete the message in gmail
        service.users().messages().delete(userId='me', id=message_id).execute()
        # update database with message deleted
        cur.execute("UPDATE spam SET msgDeleted = ? WHERE msgID = ?", (1, message_id))
        con.commit()
        print("Message deleted from gmail")
    except HttpError as e:
        print("An error occurred: %s" % e)
        print("Error deleting message")


def visualizeResults():
    try:
        connection = sqlite3.connect('spam.db')
        cursor = connection.cursor()
        # cursor.execute(
        #     'CREATE TABLE "spam" ("msgID" TEXT NOT NULL UNIQUE,"msgFrom" TEXT NOT NULL,"msgDate"	TEXT NOT NULL,"msgSeen"	NUMERIC,"msgDeleted" NUMERIC,"msgNotes"	TEXT, PRIMARY KEY("msgID"))')
        # connection.commit()
        df = pd.read_sql("SELECT msgFrom, count(*) as count FROM spam GROUP BY msgFrom ORDER BY count DESC", connection)
        # df.shape()
        print(df.head())
        print(df.describe())
        # plot df
        try:
            df = df.iloc[:20]
            ax = df.plot(kind="barh", y='count', x='msgFrom', figsize = (20, 8))
            ax.set_title('Spam Count by Sender')
            ax.set_xlabel('Count')
            ax.set_ylabel('Sender')
            plt.setp(ax.get_yticklabels(), rotation=30, ha='right')
            # valuelabels = ('count', 'msgFrom')
            # ax.set_xticklabels(df['msgFrom'], rotation=45)
            plt.show()
            # ax = df.plot(kind='bar', x='msgFrom', y='count')
            # plt.show()
        except Exception as e:
            print("Error plotting data {}".format(e))
    except sqlite3.Error as e:
        print("Error: {}".format(e.args[0]))
        con.rollback()
    finally:
        if connection:
            connection.close()


def main():
    global msg, con, cur, service
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
        messagecount = 0
        for m in messages:
            messagecount += 1
        print("Found {} messages".format(messagecount))

        if not messages:
            print('No messages found.')
        else:
            # f = None
            con = None
            try:
                con = sqlite3.connect('spam.db')
                cur = con.cursor()
                cur.execute(
                    'CREATE TABLE "spam" ("msgID" TEXT NOT NULL UNIQUE,"msgFrom" TEXT NOT NULL,"msgDate"	TEXT NOT NULL,"msgSeen"	NUMERIC,"msgDeleted" NUMERIC,"msgNotes"	TEXT, PRIMARY KEY("msgID"))')
                con.commit()
            except sqlite3.Error as e:
                print("Error: {}".format(e.args[0]))
                con.rollback()
            finally:
                if con:
                    con.close()
            try:
                message_count = int(input("How many messages do you want to see? "))
            except ValueError:
                print("Please enter a number")
                message_count = int(input("How many messages do you want to see? "))
            iter = 0
            notoall = 0
            yestoall = 0
            for message in messages[:message_count]:
                # print(message)
                # return
                iter = iter + 1
                message_id = message['id']
                msg = service.users().messages().get(userId='me', id=message_id).execute()
                print("******* Start: Message Payload Headers ({}) ********".format(iter))
                try:
                    con = sqlite3.connect('spam.db')
                    cur = con.cursor()
                except sqlite3.Error as e:
                    print("Error: {}".format(e.args[0]))
                else:
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
                        if vals['name'] == 'Date':
                            messageDate = vals['value']
                    if len(messageDate.split(',')) > 1:
                        messageDate = messageDate.split(',')[1].strip()
                    print("{0}, {1}, {2}".format(message['id'], messageFrom, messageDate))
                    message_id = message['id']
                    insertMessageDB(message_id, messageFrom, messageDate, service)
                    # print("message ID {0}".format(message_id))
                    if (notoall == 0) and (yestoall == 0):
                        # print("notoall is {0} and yestoall is {1} and ID is {2}".format(notoall, yestoall, message_id))
                        answer = input("do you want to delete all none or just this message?(none/all/this): ")
                        if answer == "none":
                            # print("The answer is \"none\"")
                            notoall = 1
                            pass
                        elif answer == "all":
                            # print("The answer is \"all\"")
                            yestoall = 1
                            pass
                        else:
                            # print("The answer is \"this\"")
                            # print("deleting message ({0})".format(index))
                            #TO DO: enable the functions to delete all messages or just the one that was selected
                            deleteMessage(message_id, service, cur, con)
                            # print("Message {0} deleted".format(message_id))
                            continue
                    if notoall == 1:
                        print("Not deleting Message {0}".format(message_id))
                        # print("not deleting message({0})".format(index))
                    elif yestoall == 1:
                        print("Deleting Message {0}".format(message_id))
                        deleteMessage(message_id, service, cur, con)
                        # print("deleting message({0})".format(index))

                    # if input("Delete the message {0} received from {1}? (y/n): ".format(message_id, messageFrom)) == 'y':
                    #     deleteMessage(message_id, service, cur, con)
                    #     print("Message {0} deleted".format(message_id))
            if con:
                con.close()
            print("******* End: Message Payload Headers **************************")
            # time.sleep(2)

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

    print("*********Visualizing the database**************************")
    if input("Do you want to Visualize the results? (y/n): ") == "y":
        visualizeResults()


if __name__ == '__main__':
    main()
