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

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    A PROGRAMAÇÃO AINDA NÃO COMEÇOU.
    Este arquivo contém apenas comentários explicativos e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DAS CLASSES DE TETRAMINÓS (INTEGRANTE 2)
# ==============================================================================

# TODO: Importar dependências:
#       from abc import ABC, abstractmethod
#       from typing import Tuple
#       from block import Block
#       from exceptions import InvalidRotationError

# TODO: Definir o alias de tipo para as formas:
#       TetriminoShape = Tuple[Block, Block, Block, Block]

# TODO: Planejar a classe base abstrata Tetrimino:
#       class Tetrimino(ABC):
#           """
#           Classe base abstrata para todos os tetraminós do jogo.
#           """
#           _NUMBER_OF_ROTATIONS: int = 4
#
#           def __init__(self, initial_rotation: int = 0):
#               # 1. Validar se initial_rotation está no intervalo [0, _NUMBER_OF_ROTATIONS - 1].
#               #    Se inválido, lançar InvalidRotationError.
#               # 2. Obter forma original através de self._original_shape().
#               # 3. Calcular self._box_size = 1 + max(max(b.x, b.y) for b in original_shape).
#               # 4. Pré-calcular as 4 rotações (armazenadas em self._shapes) aplicando
#               #    self._rotate_shape repetidamente.
#               # 5. Inicializar self._rotation = initial_rotation.
#               pass
#
#           @property
#           @abstractmethod
#           def color(self) -> str:
#               """Retorna a cor da peça no formato '#rrggbb' (somente leitura)."""
#               pass
#
#           @abstractmethod
#           def _original_shape(self) -> TetriminoShape:
#               """Método abstrato que retorna os 4 blocos da rotação 0."""
#               pass
#
#           @staticmethod
#           def _rotate_shape(shape: TetriminoShape, box_size: int) -> TetriminoShape:
#               """
#               Método estático que gira uma forma 90° no sentido horário:
#               (x, y) -> (box_size - 1 - y, x)
#               Retorna uma nova tupla de 4 instâncias de Block.
#               """
#               pass
#
#           @property
#           def box_size(self) -> int:
#               """Retorna o tamanho do lado da caixa delimitadora (somente leitura)."""
#               pass
#
#           @property
#           def shape(self) -> TetriminoShape:
#               """Retorna os blocos da rotação atual (somente leitura)."""
#               pass
#
#           @property
#           def current_rotation(self) -> int:
#               """Retorna o número da rotação atual de 0 a 3 (somente leitura)."""
#               pass
#
#           def right_rotate(self):
#               """Avança para a próxima rotação no sentido horário (0 -> 1 -> 2 -> 3 -> 0)."""
#               pass
#
#           def left_rotate(self):
#               """Volta para a rotação anterior no sentido anti-horário (0 <- 1 <- 2 <- 3 <- 0)."""
#               pass
#
#           def __str__(self) -> str:
#               """
#               Desenha a caixa delimitadora com ⬜ nas células ocupadas
#               e ⬛ nas células vazias, uma linha por y.
#               """
#               pass

# TODO: Planejar as 7 subclasses com formas e cores exatas do PDF:
#
#       class TetriminoI(Tetrimino):
#           # Forma original (0): (0,1), (1,1), (2,1), (3,1)
#           # Cor: '#00f0f0' | box_size: 4
#           pass
#
#       class TetriminoJ(Tetrimino):
#           # Forma original (0): (0,0), (0,1), (1,1), (2,1)
#           # Cor: '#0000f0' | box_size: 3
#           pass
#
#       class TetriminoL(Tetrimino):
#           # Forma original (0): (2,0), (0,1), (1,1), (2,1)
#           # Cor: '#f0a000' | box_size: 3
#           pass
#
#       class TetriminoO(Tetrimino):
#           # Forma original (0): (0,0), (1,0), (0,1), (1,1)
#           # Cor: '#f0f000' | box_size: 2
#           pass
#
#       class TetriminoS(Tetrimino):
#           # Forma original (0): (1,0), (2,0), (0,1), (1,1)
#           # Cor: '#00f000' | box_size: 3
#           pass
#
#       class TetriminoT(Tetrimino):
#           # Forma original (0): (1,0), (0,1), (1,1), (2,1)
#           # Cor: '#a000f0' | box_size: 3
#           pass
#
#       class TetriminoZ(Tetrimino):
#           # Forma original (0): (0,0), (1,0), (1,1), (2,1)
#           # Cor: '#f00000' | box_size: 3
#           pass
