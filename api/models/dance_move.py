# creating new class
import pdb
class DanceMove():
    _styles =['Street', 'Ballroom', 'Popping', 'Locking']

    def all(r):
        return {'dance_move': all_dance_moves}
    
    def create(r):
        new_dance_move = r.get_json()
        all_dance_moves.append(new_dance_move)
        new_dance_move['id'] = len(all_dance_moves)
        return new_dance_move
    
    def __init__(self, name, style, image):
        self._name = name
        self._style = style
        self._image = image
    
    def __str__(self):
            return f'{self._name} from {self._style} style'

    def step(self):
        return f'{self._name} is my favorite step!'
    
    @property
    def style(self):
        return self._style
    
    @property
    def image(self):
        return self._image
    
    #setter method
    @style.setter
    def style(self, style):
        if style in type(self)._styles:
            self._style = style
    
    @classmethod
    def list_styles():
        # for each method
        for style in _styles:
            print(style)
    
    @staticmethod
    def why():
        print('I love dancing!')

    @staticmethod
    def about():
        print('Cool!')   

    # @staticmethod
    # def index(): 
    #     return  
        
# creating new instances
indian_step = DanceMove('Indian Step', 'Street', {"id": 1, "name": 'indian_step', "url": 'https://www.wikihow.com/images/thumb/9/9f/Do-Some-Break-Dance-Moves-Step-5-Version-2.jpg/v4-460px-Do-Some-Break-Dance-Moves-Step-5-Version-2.jpg'})
egyptian_twist = DanceMove('Egyptian Twist', 'Popping',  {"id": 2, "name": 'eqyptian_twist', "url": 'https://qph.fs.quoracdn.net/main-qimg-ac6fa3279c78c85c51a6a54d4973a66d'})

pdb.set_trace()