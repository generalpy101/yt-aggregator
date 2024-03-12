from db import db

class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        """Return a dictionary representation of the model"""
        data_dict = {}

        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue
            data_dict[key] = value

        return data_dict

    @classmethod
    def filter(cls, *criterion):
        query_obj = db.session.query(cls)
        return query_obj.filter(*criterion)
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()