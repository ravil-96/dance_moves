from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import dance_moves

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello Flask!'

@app.route('/dance_moves', methods=['GET', 'POST'])
def dance_moves():
    fns = {
        'GET': all,
        'POST': create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)