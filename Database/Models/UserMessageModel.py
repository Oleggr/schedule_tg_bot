from Database.Models.AbstractModel import AbstractModel
from Controllers.DateTimeController import DateTimeController


class UserMessageModel(AbstractModel):

    table_name = 'userMessages'

    primary_key = ['message_id']

    fields = {
        primary_key[0]: '',
        'chat_id': '',
        'user_status': '',
        'message': '',
        'creation_date': ''
    }

    def get(self, primary_key):
        return super(UserMessageModel, self).get(primary_key)

    def set(self):
        self.fields['creation_date'] = int(DateTimeController.getCurrTimestamp())
        return super(UserMessageModel, self).set()

    def update(self, new_fields):
        super(UserMessageModel, self).update(new_fields)
