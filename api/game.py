from flask import Response, jsonify, current_app
import requests
from datetime import datetime
import pytz
import json

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
        print(data)
        if data:
            games = ""
            for game in data:
                game_obj = "{} vs {} @ {}".format(game['home_team']['full_name'], game['visitor_team']['full_name'], game['status'])
                games += game_obj + "\n"
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
    
