dance_moves = [
    {"id": 1, "name": 'Indian Step', "style": 'Street', "img": 'https://www.wikihow.com/images/thumb/9/9f/Do-Some-Break-Dance-Moves-Step-5-Version-2.jpg/v4-460px-Do-Some-Break-Dance-Moves-Step-5-Version-2.jpg'},
    {"id": 2, "name": 'Eqyptian Twist', "style": 'Popping', "img": 'https://qph.fs.quoracdn.net/main-qimg-ac6fa3279c78c85c51a6a54d4973a66d'},
    {"id": 3, "name": 'Muscleman', "style": 'Locking', "img": 'https://i.ytimg.com/vi/P25ZGl_h6SY/maxresdefault.jpg'}
]

def index(req):
    return [d for d in dance_moves], 200

def create(req):
    new_dance_move = req.get_json()
    new_dance_move["id"] = len(dance_moves) + 1
    dance_moves.append(new_dance_move)
    return new_dance_move, 201

