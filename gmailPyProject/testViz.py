import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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
            df = df.iloc[:10]
            ax = df.plot.barh(x='msgFrom', y='count', rot=0, color='blue',title='Top 10 Spam Senders',  figsize=(20, 8), position=0.8)
            # ax = df.plot.barh(x='count', y='msgFrom', legend=True, figsize=(20, 8))
            ax.set_title('Spam Count by Sender')
            ax.set_xlabel('Count')
            ax.set_ylabel('Sender')
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
            print("Connection closed")

def visualizeResultsDate():
    try:
        connection = sqlite3.connect('spam.db')
        cursor = connection.cursor()
        # cursor.execute(
        #     'CREATE TABLE "spam" ("msgID" TEXT NOT NULL UNIQUE,"msgFrom" TEXT NOT NULL,"msgDate"	TEXT NOT NULL,"msgSeen"	NUMERIC,"msgDeleted" NUMERIC,"msgNotes"	TEXT, PRIMARY KEY("msgID"))')
        # connection.commit()
        df = pd.read_sql("SELECT msgDate, count(msgID) as count FROM spam GROUP BY msgDate ORDER BY count ASC", connection)
        # df.shape()
        print(df.head())
        print(df.describe())
        # plot df
        try:
            df = df.iloc[:30]
            ax = df.plot.scatter(y='msgDate', x='count')
            # ax = df.plot.barh(x='count', y='msgFrom', legend=True, figsize=(20, 8))
            ax.set_title('Spam Count by Sender')
            ax.set_xlabel('Count')
            ax.set_ylabel('Date')
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
            print("Connection closed")

if __name__ == "__main__":
    visualizeResultsDate()