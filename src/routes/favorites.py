from flask import Blueprint, jsonify, request
from models import Favorite_Characters, Favorite_Planets

bpFavorite_Characters = Blueprint('bpFavorite_Characters', __name__)
bpFavorite_Planets = Blueprint('bpFavorite_Planets', __name__)

@bpFavorite_Characters.route('/favorite/character/<int:id>', methods=['POST'])
def add_favorite_character(id):
    id_user = request.json.get('id_user')

    favorite_character = Favorite_Characters()
    favorite_character.id_user = id_user
    favorite_character.id_character = id

    favorite_character.save()

    return jsonify(favorite_character.serialize()), 200


@bpFavorite_Planets.route('/favorite/planet/<int:id>', methods=['POST'])
def add_favorite_planet(id):
    id_user = request.json.get('id_user')

    favorite_planet = Favorite_Planets()
    favorite_planet.id_user = id_user
    favorite_planet.id_planets = id

    favorite_planet.save()

    return jsonify(favorite_planet.serialize()), 200


@bpFavorite_Characters.route('/favorite/character/<int:id>', methods=['DELETE'])
def delete_favorite_character(id):

    favorite_character = Favorite_Characters.query.filter_by(id_user=1,id_character=id).first()

    favorite_character.delete()

    return jsonify({"mensaje":"Favorite Character deleted."}), 201


@bpFavorite_Planets.route('/favorite/planet/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):
    favorite_planet = Favorite_Planets.query.filter_by(id_user=1,id_planets=id).first()

    favorite_planet.delete()

    return jsonify({"mensaje":"Favorite Planet deleted."}), 201