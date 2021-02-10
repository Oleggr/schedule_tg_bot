import mariadb
import subprocess

from Controllers.Db.AbstractSqlController import AbstractSqlController


class MariadbDbController(AbstractSqlController):

    def __init__(self):
        super().__init__()
        self.DB_PARAMS = {
            'user': self.config.MARIA_USERNAME,
            'password': self.config.MARIA_PASSWORD,
            'host': self.config.MARIA_HOST,
            'port': int(self.config.MARIA_PORT),
            'database': self.config.MARIA_DB,
            # 'connect_timeout': self.config.MARIA_CONN_TIMEOUT
        }
        self.conn = mariadb.connect(**self.DB_PARAMS)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """Closes cursor and conn connections when object destroys"""
        self.cursor.close()
        self.conn.close()

    def _executeQuery(self, query: str) -> int:
        """Executes SQL statement

        @param query SQL statement
        """
        self.cursor.execute(query)
        #self.conn.commit()
        return self.cursor.lastrowid

    def _fetchResult(self) -> list:
        """Fetches result from last executed SELECT statement

        @return List of rows from result table
        """
        rows = self.cursor.fetchall()
        return [row for row in rows]

    def submitQuery(self, query: str) -> int:
        """Executes INSERT or UPDATE statements

        @param query SQL statement
        """
        try:
            record_id = self._executeQuery(query)
            return record_id
        except Exception as error:
            self.logger.alert(
                f'Error while connecting to mariadb: {error}')
            print('Problem query: ', query)

    def fetchQuery(self, query: str) -> list:
        """Executes SELECT query and returns list

        @param query SQL statement
        """
        try:
            self._executeQuery(query)
            result = self._fetchResult()
            return result
        except Exception as error:
            self.logger.alert(
                f'Error while connecting to mariadb: {error}')
            print('Problem query: ', query)

    def makeDump(self):
        """Makes dump database"""
        # pg_dump --dbname=postgresql://postgres:secret@postgresql_domain:5432/database -f dump.sql
        try:
            process = subprocess.Popen(
                [
                    'mysqldump',
                    '-h', self.config.POSTGRES_HOST,
                    '-P', self.config.POSTGRES_PORT,
                    '-u -root', self.config.POSTGRES_DB,
                    '>', self.config.DUMP_FILENAME
                ],
                stdout=subprocess.PIPE
            )
            if process.returncode != 0:
                self.logger.alert(
                    f'Command failed. Return code : {process.returncode}')
        except Exception as e:
            self.logger.alert(f'Error while dumping mariaDB: {e}')
