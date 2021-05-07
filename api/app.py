from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import dance_moves

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hey! We are going to show you some dance moves in a sec!"}), 200

@app.route('/dance_moves', methods=['GET', 'POST'])
def dance_moves_handler():
    fns = {
        'GET': dance_moves.index,
        'POST': dance_moves.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

if __name__ == "__main__":
    create_app()