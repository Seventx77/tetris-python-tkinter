"""
MÓDULO: block.py
RESPONSÁVEL: Integrante 1 (Exceções e Bloco Imutável)
DESCRIÇÃO:
    Este módulo define a classe Block, representando um quadrado individual de um
    tetraminó dentro da sua caixa delimitadora, conforme especificação do professor.

CARACTERÍSTICAS OBRIGATÓRIAS (PDF DO PROFESSOR):
    - Objeto imutável.
    - Atributos internos: _x (int) e _y (int).
    - Propriedades somente leitura (@property): x (coluna) e y (linha).
    - __init__(x: int, y: int): lança InvalidBlockError se x ou y for negativo.
    - Métodos especiais convenientes: __eq__, __hash__, __repr__.

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    A PROGRAMAÇÃO AINDA NÃO COMEÇOU.
    Este arquivo contém apenas comentários explicativos e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DA CLASSE BLOCK (INTEGRANTE 1)
# ==============================================================================

# TODO: Planejar a classe Block:
#       class Block:
#           """
#           Representa um bloco imutável em coordenadas inteiras (x, y).
#           """
#
#           def __init__(self, x: int, y: int):
#               # Validar se x ou y é negativo:
#               #   if x < 0 or y < 0:
#               #       raise InvalidBlockError("Coordenadas do bloco não podem ser negativas")
#               # Armazenar em atributos privados:
#               #   self._x = x
#               #   self._y = y
#               pass
#
#           @property
#           def x(self) -> int:
#               # Retorna a coordenada horizontal x (coluna) - somente leitura
#               pass
#
#           @property
#           def y(self) -> int:
#               # Retorna a coordenada vertical y (linha) - somente leitura
#               pass
#
#           def __eq__(self, other) -> bool:
#               # Dois blocos são iguais se possuem o mesmo (x, y)
#               pass
#
#           def __hash__(self) -> int:
#               # Hash baseado em (self._x, self._y) para suportar imutabilidade
#               pass
#
#           def __repr__(self) -> str:
#               # Representação para depuração (ex: f"Block({self.x}, {self.y})")
#               pass



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
