from flask import Flask
from src.Blueprint.user import user
from src.Blueprint.car import car
from src.Blueprint.rent import rent

from flask_cors import CORS

import os

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(car)
app.register_blueprint(rent)

CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('PORT'), debug=True)
