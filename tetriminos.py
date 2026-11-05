"""
MÓDULO: tetriminos.py
RESPONSÁVEL: Integrante 2 (Peças e Rotações)
DESCRIÇÃO:
    Este módulo define a classe base abstrata Tetrimino e as 7 subclasses
    específicas correspondentes às peças clássicas do Tetris (I, J, L, O, S, T, Z),
    conforme as especificações exatas e o diagrama UML do professor.

CONCEITOS DE OO E ESPECIFICAÇÕES DO PROFESSOR:
    - type TetriminoShape = tuple[Block, Block, Block, Block]
    - Constante _NUMBER_OF_ROTATIONS: int = 4
    - A peça NÃO conhece o tabuleiro (não sabe sua posição nem verifica colisões).
    - Cálculo de box_size: 1 + maior valor entre todos os x e y dos blocos da forma original.
    - Fórmula de rotação horária de 90°: (x, y) ──> (box_size - 1 - y, x).
    - Métodos de rotação oficiais: right_rotate() (sentido horário) e left_rotate() (sentido anti-horário).
    - Método __str__() para renderizar a caixa no terminal com ⬜ nas células ocupadas e ⬛ nas vazias.
"""


from abc import ABC, abstractmethod
from typing import Tuple
from block import Block
from exceptions import InvalidRotationError

TetriminoShape = Tuple[Block, Block, Block, Block]

class Tetrimino(ABC):
    """
    Classe base abstrata para todos os tetraminós do jogo.
    """
    _NUMBER_OF_ROTATIONS: int = 4

    def __init__(self, initial_rotation: int = 0):
        if initial_rotation < 0 or initial_rotation > self._NUMBER_OF_ROTATIONS - 1:
            raise InvalidRotationError("Invalid initial rotation value.")

        self._rotation = initial_rotation
        original_shape = self.original_shape()
        self._shapes = [original_shape]

        self._box_size = 1 + max(max(b.x, b.y) for b in original_shape)
        for _ in range(3):
            novo_shape = self._rotate_shape(self._shapes[-1], self.box_size)
            self._shapes.append(novo_shape)
        
    @staticmethod
    def _rotate_shape(forma, box_size: int) -> TetriminoShape:
            """
            Método estático que gira uma forma 90° no sentido horário:
            (x, y) -> (box_size - 1 - y, x)
            Retorna uma nova tupla de 4 instâncias de Block.
            """
            nova_forma = []
            for bloco in forma:
                nova_forma.append(Block((box_size - 1 - bloco.y), bloco.x))
            nova_forma = tuple(nova_forma)
            return nova_forma
        
     

    @abstractmethod
    def original_shape(self) -> TetriminoShape:
        """Método abstrato que retorna os 4 blocos da rotação 0."""
        pass

    @property
    @abstractmethod
    def color(self) -> str:
         pass

    @property
    def box_size(self):
        return self._box_size

    @property
    def shape(self) -> TetriminoShape:
        """Retorna os blocos da rotação atual (somente leitura)."""
        return self._shapes[self._rotation]
    @property
    def current_rotation(self) -> int:
        """Retorna o número da rotação atual de 0 a 3 (somente leitura)."""
        return self._rotation

    def right_rotate(self):
        """Avança para a próxima rotação no sentido horário (0 -> 1 -> 2 -> 3 -> 0)."""
        t = self._rotation + 1
        if t  == 4:
            self._rotation = 0
        else:
            self._rotation +=1
    

    def left_rotate(self):
        """Volta para a rotação anterior no sentido anti-horário (0 <- 1 <- 2 <- 3 <- 0)."""
        if self._rotation == 0:
            self._rotation = 3
        else:
            self._rotation -= 1

    def __str__(self) -> str:
        """
        Desenha a caixa delimitadora com ⬜ nas células ocupadas
        e ⬛ nas células vazias, uma linha por y.
        """
        r =''
        for y in range(self.box_size):
            for x in range(self.box_size):
                ocupado = False
                for i in self.shape:
                    if x == i.x and y == i.y:
                        ocupado = True

                if ocupado == True:
                        r += '⬜'
                else:
                        r+='⬛'
            r+='\n'
        return r
                     


class TetriminoI(Tetrimino):

         
    @property
    def color(self):
         return '#00f0f0'
    def original_shape(self):
         forma = (Block(0,1), Block(1,1), Block(2,1), Block(3,1))
         return forma

class TetriminoJ(Tetrimino):

    @property
    def color(self):
        return '#0000f0'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(0, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
        return forma


class TetriminoL(Tetrimino):

    @property
    def color(self):
        return '#f0a000'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(2, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
        return forma


class TetriminoO(Tetrimino):

    @property
    def color(self):
        return '#f0f000'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(0, 0),
            Block(1, 0),
            Block(0, 1),
            Block(1, 1)
        )
        return forma


class TetriminoS(Tetrimino):

    @property
    def color(self):
        return '#00f000'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(1, 0),
            Block(2, 0),
            Block(0, 1),
            Block(1, 1)
        )
        return forma


class TetriminoT(Tetrimino):

    @property
    def color(self):
        return '#a000f0'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(1, 0),
            Block(0, 1),
            Block(1, 1),
            Block(2, 1)
        )
        return forma


class TetriminoZ(Tetrimino):

    @property
    def color(self):
        return '#f00000'

    def original_shape(self) -> TetriminoShape:
        forma = (
            Block(0, 0),
            Block(1, 0),
            Block(1, 1),
            Block(2, 1)
        )
        return forma




        
if __name__ == '__main__':
    pecas = [
        TetriminoI(),
        TetriminoJ(),
        TetriminoL(),
        TetriminoO(),
        TetriminoS(),
        TetriminoT(),
        TetriminoZ()
    ]

    for peca in pecas:
        print(f'{peca.__class__.__name__}')
        print(peca)
        print(f'Cor: {peca.color}')
        print(f'Tamanho: {peca.box_size}')
        print('-' * 20)

