#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /0-hbnb/: HBnB home page.
"""
from models import storage
from flask import Flask, render_template
import uuid

app = Flask(__name__)

@app.route("/0-hbnb/", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    cache_id = uuid.uuid4()
    return render_template("0-hbnb.html",
                           states=states, amenities=amenities, places=places, cache_id=cache_id)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
