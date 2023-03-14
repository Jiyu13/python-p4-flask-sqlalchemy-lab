from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.DateTime)

    animals = db.relationship('Animal', backref='zookeeper')

    def __repr__(self):
        return f"<Zookeeper {self.id}: {self.name}, birthday: {self.birthday}>"


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure') # pets.enclosure

    def __repr__(self):
        return f"<Enclosure {self.id}: {self.environment}, open: {self.open_to_visitors}>"
    

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.String, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f"<Animal {self.name}, {self.species}, zookeeper: {self.zookeeper}, enclosure: {self.enclosure}>"
