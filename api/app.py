from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import dance_moves

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hey! We are going to show you some dance moves in a sec!'

@app.route('/dance_moves', methods=['GET', 'POST'])
def dance_moves_handler():
    fns = {
        'GET': dance_moves.index,
        'POST': dance_moves.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)