import sqlalchemy as db
from base import Base


class Todo(Base):

    __tablename__ = "todo"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    title = db.Column("title", db.String(15), nullable=False)
    descraibe = db.Column("descraibe", db.String(50))

    def __init__(self, title, descraibe):
        self.title = title
        self.descraibe = descraibe
