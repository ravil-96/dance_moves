from models import dance_move

def index(req):
    return dance_moves, 200

def create(req):
    new_dance_move = req.get_json()
    new_dance_move["id"] = len(dance_moves) + 1
    dance_moves.appemd(new_dance_move)
    return new_dance_move, 201

