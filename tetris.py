"""
MÓDULO: tetris.py
RESPONSÁVEL: Integrante 3 (Modelo do Jogo e Regras de Negócio)

Modelo do jogo: tabuleiro 10x18, peça ativa, movimentos, colisões,
fixação (_lock) e eliminação de linhas. Não tem print, input nem interface.

Convenções (PDF do professor):
  - _grid[coluna][linha] guarda a cor '#rrggbb' ou None se vazia
  - x = coluna (esquerda -> direita), y = linha (cima -> baixo)
  - (_tetri_col, _tetri_row) é o canto superior esquerdo da caixa da peça
"""

import random
from typing import List, Optional, Tuple

from tetriminos import (
    Tetrimino, TetriminoI, TetriminoJ, TetriminoL,
    TetriminoO, TetriminoS, TetriminoT, TetriminoZ,
)


class Tetris:
    DEFAULT_WIDTH: int = 10
    DEFAULT_HEIGHT: int = 18
    _TETRIMINOS = (
        TetriminoI, TetriminoJ, TetriminoL, TetriminoO,
        TetriminoS, TetriminoT, TetriminoZ,
    )

    def __init__(self):
        self._grid: List[List[Optional[str]]] = []
        self._tetri_active: Optional[Tetrimino] = None
        self._tetri_col: int = 0
        self._tetri_row: int = 0
        self._game_over: bool = False
        self.reset()


    @property
    def width(self) -> int:
        return self.DEFAULT_WIDTH

    @property
    def height(self) -> int:
        return self.DEFAULT_HEIGHT

    @property
    def game_over(self) -> bool:
        return self._game_over

    @property
    def active_tetrimino(self) -> Optional[Tetrimino]:
        return self._tetri_active

    def color_at(self, column: int, row: int) -> Optional[str]:
        """Cor da célula, considerando também a peça ativa. None se vazia."""
        if self._tetri_active is not None:
            if (column, row) in self._tetri_cells(self._tetri_col, self._tetri_row):
                return self._tetri_active.color
        if 0 <= column < self.width and 0 <= row < self.height:
            return self._grid[column][row]
        return None


    def reset(self):
        """Limpa o tabuleiro, desfaz o fim de jogo e sorteia uma nova peça."""
        self._grid = [[None] * self.height for _ in range(self.width)]
        self._game_over = False
        self._new_tetrimino()

    def move_left(self):
        if self._game_over:
            return
        if self._tetri_fits(self._tetri_col - 1, self._tetri_row):
            self._tetri_col -= 1

    def move_right(self):
        if self._game_over:
            return
        if self._tetri_fits(self._tetri_col + 1, self._tetri_row):
            self._tetri_col += 1

    def move_down(self):
        """Desce uma linha. Se não couber, fixa a peça."""
        if self._game_over:
            return
        if self._tetri_fits(self._tetri_col, self._tetri_row + 1):
            self._tetri_row += 1
        else:
            self._lock()

    def drop(self):
        """Desce até onde conseguir e fixa a peça."""
        if self._game_over:
            return
        while self._tetri_fits(self._tetri_col, self._tetri_row + 1):
            self._tetri_row += 1
        self._lock()

    def rotate(self):
        """Gira no sentido horário. Se não couber, desfaz o giro."""
        if self._game_over:
            return
        self._tetri_active.right_rotate()
        if not self._tetri_fits(self._tetri_col, self._tetri_row):
            self._tetri_active.left_rotate()

    
    def _tetri_cells(self, col: int, row: int) -> List[Tuple[int, int]]:
        """Células do tabuleiro que a peça ativa ocuparia com a caixa em (col, row)."""
        return [(col + bloco.x, row + bloco.y) for bloco in self._tetri_active.shape]

    def _tetri_fits(self, col: int, row: int) -> bool:
        """True se todos os blocos estão dentro do tabuleiro e em células vazias."""
        for c, r in self._tetri_cells(col, row):
            if c < 0 or c >= self.width or r < 0 or r >= self.height:
                return False
            if self._grid[c][r] is not None:
                return False
        return True

    def _new_tetrimino(self):
        """Sorteia uma peça, centraliza no topo e marca fim de jogo se não couber."""
        peca = random.choice(self._TETRIMINOS)()
        self._tetri_active = peca
        self._tetri_col = (self.width - peca.box_size) // 2
        self._tetri_row = 0
        if not self._tetri_fits(self._tetri_col, self._tetri_row):
            self._game_over = True

    def _lock(self):
        """Grava a peça no _grid, remove linhas completas e cria nova peça."""
        cor = self._tetri_active.color
        for c, r in self._tetri_cells(self._tetri_col, self._tetri_row):
            self._grid[c][r] = cor
        self._clear_rows()
        self._new_tetrimino()

    def _clear_rows(self) -> int:
        """Remove as linhas completas, descendo as de cima. Retorna quantas removeu."""
        removidas = 0
        r = self.height - 1
        while r >= 0:
            if all(self._grid[c][r] is not None for c in range(self.width)):
                for rr in range(r, 0, -1):
                    for c in range(self.width):
                        self._grid[c][rr] = self._grid[c][rr - 1]
                for c in range(self.width):
                    self._grid[c][0] = None
                removidas += 1
                
            else:
                r -= 1
        return removidas
