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

