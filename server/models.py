from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.DateTime)
    animals = db.relationship('Animal', backref="zookeeper")    # animal.zookeeper

    def __repr__(self):
        return f'''<Zookeeper ID: {self.id}\nName: {self.name}\nBirthday: {self.birthday}\n'''


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref="enclosure")

    def __repr__(self):
        return f'''<Enclosure ID: {self.id}\Environment: {self.environment}\nOpen_to_visitors: {self.open_to_visitors}\n'''
   

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    enclosure_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"))

    def __repr__(self):
        return f'''<Animal ID: {self.id}\nName: {self.name}\nspecies: {self.species}\n'''
