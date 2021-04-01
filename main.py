

from flask_cors import CORS
from flask import Flask, request
from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
