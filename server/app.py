#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter_by(id=id).first()
    zookeeper = animal.zookeeper
    animal_dict = {
        "name": animal.name,
        "species": animal.species,
        "zookeeper": {
            "name": zookeeper.name,
            "birthday": zookeeper.birthday
        }
    }
    return make_response(animal_dict, 200)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter_by(id=id).first()
    animals_dict = []
    for animal in zookeeper.animals:
        animal_dict = {
            "name": animal.name,
            "species": animal.species
        }
        animals_dict.append(animal_dict)
    zookeeper_dict = {
        "name": zookeeper.name,
        "birthday": zookeeper.birthday,
        "animals": animals_dict
    }
    return make_response(zookeeper_dict, 200)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter_by(id=id).first()
    animals_dict = []
    for animal in enclosure.animals:
        animal_dict = {
            "name": animal.name,
            "species": animal.species
        }
        animals_dict.append(animal_dict)
    enclosure_dict = {
        "environment": enclosure.environment,
        "open_to_visitors": enclosure.open_to_visitors,
        "animals": animals_dict
    }
    return make_response(enclosure_dict, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
