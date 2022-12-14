from flask import Blueprint, jsonify, request
from models import Characters

bpCharacters = Blueprint('bpCharacters', __name__)

@bpCharcters.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    if not characters: return jsonify({ "message": "Empty route. You may need to post some data."}), 404
    characters = list(map(lambda character: characters.serialize(), characters))
    return jsonify(characters), 200

@bpCharacters.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
     characters = Characters.query.get(id)
     return jsonify(characters.serialize()), 201

@bpCharacters.route('/characters', methods=['POST'])
def add_character():
    id = request.json.get('id')
    name = request.json.get('name')
    height = request.json.get('height')
    mass = request.json.get('mass')
    hair_color = request.json.get('hair_color')
    skin_color = request.json.get('skin_color')
    birth_year = request.json.get('birth_year')
    gender = request.json.get('gender')

    character = character()
    character.id = id
    character.name = name
    character.height = height
    character.mass = mass
    character.hair_color = hair_color
    character.skin_color = skin_color
    character.birth_year = birth_year
    character.gender = gender

    character.save()

    return jsonify(characters.serialize()), 203

@bpUsers.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    id = request.json.get('id')
    name = request.json.get('name')
    height = request.json.get('height')
    mass = request.json.get('mass')
    hair_color = request.json.get('hair_color')
    skin_color = request.json.get('skin_color')
    birth_year = request.json.get('birth_year')
    gender = request.json.get('gender')

    character = Character.query.get(id)
    character.id = id
    character.name = name
    character.height = height
    character.mass = mass
    character.hair_color = hair_color
    character.skin_color = skin_color
    character.birth_year = birth_year
    character.gender = gender

    character.update()

    return jsonify(characters.serialize()), 204

@bpCharacters.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    id = request.json.get('id')
    name = request.json.get('name')
    height = request.json.get('height')
    mass = request.json.get('mass')
    hair_color = request.json.get('hair_color')
    skin_color = request.json.get('skin_color')
    birth_year = request.json.get('birth_year')
    gender = request.json.get('gender')

    character = Character.query.get(id)
    character.id = id
    character.name = name
    character.height = height
    character.mass = mass
    character.hair_color = hair_color
    character.skin_color = skin_color
    character.birth_year = birth_year
    character.gender = gender
    
    character.delete()

    return jsonify(characters.serialize()), 205