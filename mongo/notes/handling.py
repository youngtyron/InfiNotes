from notes.models import Note
import datetime

class ThemeHandler(object):

    @staticmethod
    def collection(db):
        collection = db.notes_collection
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
    def create(self, db, theme_id, subtheme, text, footnote):
        date = datetime.datetime.utcnow()
        new_note = Note(theme_id, subtheme, text, footnote, date)
        collection = self.collection(db)
        collection.insert_one({
                            'theme_id': new_note.theme_id,
                            'subtheme': new_note.subtheme,
                            'text': new_note.text,
                            'footnote': new_note.footnote,
                            'date': new_note.date
                        })
        return "Заметка добавлена"

    @staticmethod
    def update():
        return

    @staticmethod
    def delete():
        return
