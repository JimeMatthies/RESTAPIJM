from flask import Blueprint, jsonify, request
from models import Users

bpUsers = Blueprint('bpUsers', __name__)

@bpUsers.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    if not users: return jsonify({ "message": "Empty route. You may need to post some data."}), 404
    users = list(map(lambda user: users.serialize(), users))
    return jsonify(users), 200

@bpUsers.route('/users', methods=['POST'])
def add_user():
    id = request.json.get('id')
    email = request.json.get('email')
    password = request.json.get('password')
    verified = request.json.get('verified')

    user = User()
    user.id = id
    user.email = email
    user.password = password
    user.verified = verified

    user.save()

    return jsonify(users.serialize()), 201

@bpUsers.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    email = request.json.get('email')
    password = request.json.get('password')
    verified = request.json.get('verified')

    user = User.query.get(id)
    user.username = username
    user.password = password
    user.verified = verified

    user.update()

    return jsonify(user.serialize()), 202

@bpUsers.route('/users/status/<status>', methods=['GET'])
def users_by_status(status):
    verified = True if status == 'activos' else False
    users = User.query.filter_by(verified=verified)
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 203

@bpUsers.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    favorites = Users.query.all()
    favorites = list(map(lambda favorite: favorites.serialize_with_favorites(), favorites))
    return jsonify(favs), 204