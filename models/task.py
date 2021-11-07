
from app import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
