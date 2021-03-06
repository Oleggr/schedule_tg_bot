from Database.Migrations.Migration import Migration
from Database.Models.TelegramUserModel import TelegramUserModel


class TelegramUsersTableMigration(Migration):

    def getDescription(self):
        print("Create UsersTable migration")

    def up(self):
        query = '''CREATE TABLE ''' + TelegramUserModel.table_name + ''' (
                user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
                chat_id INTEGER NOT NULL,
                first_name BLOB,
                last_name BLOB,
                username BLOB,
                language_code TEXT DEFAULT 'en',
                is_bot INTEGER,
                is_alive INTEGER,
                registration_date INTEGER,
                university_id INTEGER,
                group_id INTEGER,
                CONSTRAINT AK_chat_id UNIQUE(chat_id));'''

        self.dbController.submitQuery(query)
        self.logger.info("TelegramUsersTableMigration up")

    def down(self):
        query = 'DROP TABLE ' + TelegramUserModel.table_name + ';'
        self.dbController.submitQuery(query)
        self.logger.info("TelegramUsersTableMigration down")
