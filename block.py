

'''Código principal do módulo block.py'''
from exceptions import InvalidBlockError

class  Block:
    def __init__(self, x:int, y:int):
        if x < 0 or y < 0:
            raise InvalidBlockError("Coordenadas do bloco não podem ser negativas")
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y


    def __eq__(self, other):
        if isinstance(other, Block):
            return self._x == other._x and self._y == other._y
        return False
    def __hash__(self):
        return hash((self._x, self._y))
    def __repr__(self):
        return f"Block({self._x}, {self._y})"
