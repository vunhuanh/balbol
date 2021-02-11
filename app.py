import os
port = int(os.environ.get("PORT", 5000))
from flask import Flask
app = Flask(__name__)

# APIs
import api.game as Game

@app.route('/')
def hello_world():
    return 'nba schedule reminders 🏀'

@app.route('/get_today_games')
def get_today_games():
    return Game.get_today_games()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)