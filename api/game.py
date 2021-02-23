from flask import Blueprint, Response, jsonify, current_app
import requests
from datetime import datetime, date, timedelta
from dateutil import parser
import pytz
import json
import time
import os

# models
from models.game import Game

# helper
import api.email_helper as email


game_bp = Blueprint(__name__, "game_bp")

@game_bp.route("/get_today_games")
def get_today_games():
    not_found = Response(
        "No games today",
        404, 
        mimetype='application/json'
    )

    today = datetime.now(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d')
    url = "https://www.balldontlie.io/api/v1/games?start_date={}&end_date={}".format(today, today)
    response = requests.get(url)
    if response.status_code == 200 and response.content:
        jsonResponse = json.loads(response.content)
        data = jsonResponse['data']
        if data:
            games = ""
            for game in data:
                game_name = "{} vs {}".format(game['home_team']['full_name'], game['visitor_team']['full_name'])
                game_time = game['status']
                game_obj = "{} @ {}".format(game_name, game_time)
                games += game_obj + "\n"

                # Save to DB
                try:
                    time = "{} {}".format(today, game_time)
                    time = parser.parse(time)
                    new_game = Game.create_game({
                        "name": game_name,
                        "time": time
                    })
                except Exception:
                    print("Error saving game")

            email.send_email("Today's games", games)
            return Response(
                games,
                200, 
                mimetype='application/json'
            )
        else:
            return not_found
    elif response.status_code == 404:
        return not_found
    else:
        return Response(
            "Error fetching data",
            500, 
            mimetype='application/json'
        )
    
@game_bp.route("/notify_games")
def notify_games():
    games = "Updated\n"

    lower_bound = datetime.now() 
    upper_bound = datetime.now() + timedelta(minutes=15)

    today_games = Game.query.filter(Game.time.between(lower_bound, upper_bound)).filter(Game.sent_alert != True).all()
    for game in today_games:
        gtime = game.time
        msg = f"{game.name} @ {gtime.strftime('%H:%M')}"
        games += msg + "\n"
        email.send_email("Game alert", msg)
        updatedGame = Game.mark_as_alerted(game.id)

    return Response(
        games,
        200, 
        mimetype='application/json'
    )