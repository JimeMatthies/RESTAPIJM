from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    verified = db.Column(db.Boolean(), default=True)
    favorite_characters = db.relationship('Favorite_Characters')
    favorite_planets = db.relationship('Favorite_Planets')

    def __repr__(self):
        return '<Users %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "verified": self.verified
        }

    def serialize_with_favorites(self):
        favorite_characters = [characters.serialize()
                               for characters in self.favorite_characters]
        favorite_planets = [planets.serialize()
                            for planets in self.favorite_planets]

        return {
            "id": self.id,
            "email": self.email,
            "favorite_list": favorite_characters+favorite_planets
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Characters(db.Model):
    __tablename__ = 'characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(200))
    skin_color = db.Column(db.String(200))
    birth_year = db.Column(db.String(200))
    gender = db.Column(db.String(200))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planets(db.Model):
    __tablename__ = 'planets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(200))
    gravity = db.Column(db.String(200))
    terrain = db.Column(db.String(200))
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favorite_Characters(db.Model):
    __tablename__="favorite_characters"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_character = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    characters = db.relationship('Characters')

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "name": self.characters.name
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_Planets(db.Model):
    __tablename__="favorite_planets"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    planets = db.relationship('Planets')

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "name": self.planets.name
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()