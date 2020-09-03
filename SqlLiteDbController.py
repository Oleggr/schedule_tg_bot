import os
import sqlite3


class SqlLiteDbController:

    dbFilename = 'sqlite.db'

    def openConnection(self):
        self.sqliteConnection = sqlite3.connect(self.dbFilename)
        self.cursor = self.sqliteConnection.cursor()

    def executeQuery(self, query):
        self.cursor.execute(query)

    def commitQuery(self):
        self.sqliteConnection.commit()

    def closeConnection(self):
        self.cursor.close()
        self.sqliteConnection.close()

    def fetchResult(self):
        rows = self.cursor.fetchall()
        result = []

        for row in rows:
            result.append(row)

        return result

    def submitQuery(self, query):
        try:
            self.openConnection()
            self.executeQuery(query)
            self.commitQuery()
            self.closeConnection()
            
        except sqlite3.Error as error:
            print('Error while connecting to database {}'.format(error))

    def fetchQuery(self, query):
        try:
            self.openConnection()
            self.executeQuery(query)
            result = self.fetchResult()
            self.closeConnection()
            return result

        except sqlite3.Error as error:
            print('Error while connecting to database {}'.format(error))

    def db_drop(self):
        try:
            os.remove(self.dbFilename)
            print('DB was deleted')
        except Exception as e:
            print("Error while deleting db {}".format(e))
