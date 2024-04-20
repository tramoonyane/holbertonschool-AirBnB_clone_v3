#!/usr/bin/python3
# api/v1/app.py
import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
