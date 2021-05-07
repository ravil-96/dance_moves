from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import dance_moves
from werkzeug import exceptions


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

@app.route('/api/cats/<int:cat_id>')
def dance_moves_handler(move_id):
    fns = {
        'GET': dance_moves.show,
    }
    dance_move = all_dance_moves[move_id-1]
    return jsonify(dance_move)