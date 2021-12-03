from hw_app import db


class AddressBook(db.Model):
    __tablename__ = 'address_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    birthday = db.Column(db.Date)
    street = db.Column(db.String)

    def __init__(self, name, phone, email, birthday, street):
        self.name = name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.street = street


class NoteBook(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    note = db.Column(db.String)
    tags = db.Column(db.ARRAY(db.String))
    added_at = db.Column(db.Date)

    def __init__(self, title, note, tags, added_at):
        self.title = title
        self.note = note
        self.tags = tags
        self.added_at = added_at
