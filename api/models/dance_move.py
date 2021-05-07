# creating new class
import pdb

class DanceMove():
    _styles =['Street', 'Ballroom', 'Popping', 'Locking']
    
    def __init__(self, name, style, img):
        self._name = name
        self._style = style
        self._img = img
    
    def __str__(self):
            return f'{self._name} from {self._style} style'
    
    @property
    def style(self):
        return self._style
    
    @property
    def image(self):
        return self._img
    
    #setter method
    @style.setter
    def style(self, style):
        if style in type(self)._styles:
            self._style = style
    
    def index(req):
        pass

    def create(r):
        new_dance_move = r.get_json()
        all_dance_moves.append(new_dance_move)
        new_dance_move['id'] = len(all_dance_moves)
        return new_dance_move

    # @staticmethod
    # def index(): 
    #     return  
    

pdb.set_trace()