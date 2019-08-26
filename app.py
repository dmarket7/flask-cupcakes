"""Flask app for Cupcakes"""
from flask import Flask, redirect, render_template, request, flash, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SECRET_KEY"] = "any secret name"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///cupcakes'
app.config["SQLALCHEMY_TRACK_MODIFCATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

def serialize_cupcake(cupcake):
    """ Serialize a cupcake """

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route('/api/cupcakes')
def get_cupcakes():
    """ Get list of all cupcakes """

    cupcakes_from_db = Cupcake.query.all()
    serialized_cupcakes = [serialize_cupcake(cupcake) for cupcake in cupcakes_from_db]

    return jsonify(cupcakes=serialized_cupcakes)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """ Get one cupcake"""

    cupcake_from_db = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = serialize_cupcake(cupcake_from_db)

    return jsonify(cupcake=serialized_cupcake)


@app.route('/api/cupcakes', methods=["POST"])
def create_new_cupcake():
    """ Create new cupcake"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]


    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake=serialized_cupcake), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ Updates existing cupcake"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    
    cupcake_from_db = Cupcake.query.get_or_404(cupcake_id)
    cupcake_from_db.flavor = flavor
    cupcake_from_db.size = size
    cupcake_from_db.rating = rating
    cupcake_from_db.image = image

    db.session.add(cupcake_from_db)
    db.session.commit()

    serialized_cupcake = serialize_cupcake(cupcake_from_db)

    return (jsonify(cupcake=serialized_cupcake))


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes an existing cupcake"""

    cupcake_from_db = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake_from_db)
    db.session.commit()


    return (jsonify({"message": "Cupcake deleted"}))



@app.route('/')
def show_cupcakes_list():
    return render_template("home.html")
