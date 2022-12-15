from flask import Blueprint, jsonify, request
from models import Planets

bpPlanets = Blueprint('bpPlanets', __name__)

@bpPlanets.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    if not planets: return jsonify({ "message": "Empty route. You may need to post some data."}), 400
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@bpPlanets.route('/planets/<int:id>', methods=['GET'])
def get_planet(id):
    planet = Planets.query.get(id)
    return jsonify(planet.serialize()), 201

@bpPlanets.route('/planets', methods=['POST'])
def add_planet():
    id = request.json.get('id')
    name = request.json.get('name')
    rotation_period = request.json.get('rotation_period')
    orbital_period = request.json.get('orbital_period')
    diameter = request.json.get('diameter')
    climate = request.json.get('climate')
    gravity = request.json.get('gravity')
    terrain = request.json.get('terrain')
    surface_water = request.json.get('surface_water')
    population = request.json.get('population')

    planet = Planets()
    planet.id = id
    planet.name = name
    planet.rotation_period = rotation_period
    planet.orbital_period = orbital_period
    planet.diameter = diameter
    planet.climate = climate
    planet.gravity = gravity
    planet.terrain = terrain
    planet.surface_water = surface_water
    planet.population = population

    planet.save()

    return jsonify(planet.serialize()), 202

@bpPlanets.route('/planets/<int:id>', methods=['PUT'])
def update_planet(id):
    id = request.json.get('id')
    name = request.json.get('name')
    rotation_period = request.json.get('rotation_period')
    orbital_period = request.json.get('orbital_period')
    diameter = request.json.get('diameter')
    climate = request.json.get('climate')
    gravity = request.json.get('gravity')
    terrain = request.json.get('terrain')
    surface_water = request.json.get('surface_water')
    population = request.json.get('population')

    planet = Planets.query.get(id)
    planet.id = id
    planet.name = name
    planet.rotation_period = rotation_period
    planet.orbital_period = orbital_period
    planet.diameter = diameter
    planet.climate = climate
    planet.gravity = gravity
    planet.terrain = terrain
    planet.surface_water = surface_water
    planet.population = population

    planet.update()

    return jsonify(planet.serialize()), 203

@bpPlanets.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planets.query.filter_by(id=id).first()
 
    planet.delete()

    return jsonify({"mensaje":"Planet deleted."}), 204