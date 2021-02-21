import os
from flask import Flask
from config import *
from db import db
from datetime import datetime

# Models
from models.game import Game

# APIs
from api.game import game_bp

def create_app():
    app = Flask(__name__)
    app = _setup_db(app)
    _setup_blueprints(app)

    @app.route('/')
    def index():
        all_games = Game.query.filter().all()
        print(all_games)
        return 'nba schedule reminders 🏀'

    return app

def _setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        from models.game import Game
        db.create_all()
        db.session.commit()

    return app

def _setup_blueprints(app):
    app.register_blueprint(game_bp)

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)