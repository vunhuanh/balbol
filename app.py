import os
port = int(os.environ.get("PORT", 5000))
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_game')
def get_game():
    return 'lebron'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)