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

@app.route('/api/cats/<int:cat_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def dance_moves_handler(move_id):
    fns = {
        'GET': dance_moves.show,
        'PATCH': dance_moves.update,
        'PUT': dance_moves.update,
        'DELETE': dance_moves.destroy
    }
    resp, code = fns[request.method](request, move_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)