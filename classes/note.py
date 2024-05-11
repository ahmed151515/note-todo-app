import sqlalchemy as db
from base import Base


class Note(Base):

    __tablename__ = "note"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column("title", db.String(15))
    text = db.Column("text", db.String(15))

    def __init__(self, title, text):
        self.title = title
        self.text = text
