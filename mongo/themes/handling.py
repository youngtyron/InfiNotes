from themes.models import Theme
import datetime

class ThemeHandler(object):

    @staticmethod
    def collection(db):
        collection = db.themes_collection
        return collection

    @classmethod
    def list(self, db):
        collection = self.collection(db)
        list = collection.find()
        return list

    @staticmethod
    def get():
        return

    @classmethod
    def create(self, db, theme):
        date = datetime.datetime.utcnow()
        new_theme = Theme(theme, date)
        collection = self.collection(db)
        collection.insert_one({'theme': new_theme.theme, 'date': new_theme.date})
        return "Тема добавлена"

    @staticmethod
    def update():
        return

    @staticmethod
    def delete():
        return
