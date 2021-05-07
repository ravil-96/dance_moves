from models.dance_move import DanceMove
import data

movesData = data

def set_moves():
    for move in movesData:
        DanceMove(move)
    return move