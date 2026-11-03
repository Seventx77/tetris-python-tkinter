import os
import sys
import types
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# ----------------------------------------------------------------------
# Peças falsas, usadas enquanto tetriminos.py (Integrante 2) não existir.
# Se as classes reais já existirem, elas são usadas no import do tetris.
# ----------------------------------------------------------------------
from collections import namedtuple

Bloco = namedtuple("Bloco", "x y")


class PecaBase:
    color = "#ff0000"
    _forma = ((0, 0), (1, 0), (0, 1), (1, 1))
    box_size = 2

    def __init__(self):
        self._rot = 0

    @property
    def shape(self):
        blocos = list(self._forma)
        for _ in range(self._rot):
            blocos = [(self.box_size - 1 - y, x) for x, y in blocos]
        return tuple(Bloco(x, y) for x, y in blocos)

    @property
    def current_rotation(self):
        return self._rot

    def right_rotate(self):
        self._rot = (self._rot + 1) % 4

    def left_rotate(self):
        self._rot = (self._rot - 1) % 4


class PecaO(PecaBase):
    pass


class PecaI(PecaBase):
    color = "#00f0f0"
    _forma = ((0, 1), (1, 1), (2, 1), (3, 1))
    box_size = 4


try:
    from tetriminos import TetriminoI  # noqa: F401
except ImportError:
    fake = types.ModuleType("tetriminos")
    fake.Tetrimino = PecaBase
    for nome in ("I", "J", "L", "O", "S", "T", "Z"):
        setattr(fake, "Tetrimino" + nome, PecaO)
    sys.modules["tetriminos"] = fake

from tetris import Tetris


class JogoO(Tetris):
    """Tetris que só sorteia a peça O (resultado previsível)."""
    _TETRIMINOS = (PecaO,)


class JogoI(Tetris):
    """Tetris que só sorteia a peça I."""
    _TETRIMINOS = (PecaI,)


def encher_linha(jogo, r, exceto=()):
    for c in range(jogo.width):
        if c not in exceto:
            jogo._grid[c][r] = "#aaaaaa"


class TestInicio(unittest.TestCase):
    def test_tamanho_do_tabuleiro(self):
        jogo = JogoO()
        self.assertEqual((jogo.width, jogo.height), (10, 18))

    def test_peca_nasce_centralizada_no_topo(self):
        jogo = JogoO()
        self.assertEqual((jogo._tetri_col, jogo._tetri_row), (4, 0))
        self.assertEqual(jogo.color_at(4, 0), "#ff0000")
        self.assertIsNone(jogo.color_at(0, 0))

    def test_nao_comeca_em_game_over(self):
        self.assertFalse(JogoO().game_over)


class TestCabe(unittest.TestCase):
    def test_paredes_e_chao(self):
        jogo = JogoO()
        self.assertFalse(jogo._tetri_fits(-1, 0))
        self.assertFalse(jogo._tetri_fits(9, 0))
        self.assertTrue(jogo._tetri_fits(8, 0))
        self.assertFalse(jogo._tetri_fits(4, 17))
        self.assertTrue(jogo._tetri_fits(4, 16))

    def test_bloco_fixado(self):
        jogo = JogoO()
        jogo._grid[4][10] = "#00f0f0"
        self.assertFalse(jogo._tetri_fits(4, 9))
        self.assertTrue(jogo._tetri_fits(6, 9))


class TestMovimentos(unittest.TestCase):
    def test_esquerda_para_na_parede(self):
        jogo = JogoO()
        for _ in range(10):
            jogo.move_left()
        self.assertEqual(jogo._tetri_col, 0)

    def test_direita_para_na_parede(self):
        jogo = JogoO()
        for _ in range(10):
            jogo.move_right()
        self.assertEqual(jogo._tetri_col, 8)

    def test_descer_uma_linha(self):
        jogo = JogoO()
        jogo.move_down()
        self.assertEqual(jogo._tetri_row, 1)

    def test_movimento_bloqueado_por_bloco_fixado(self):
        jogo = JogoO()
        jogo._grid[3][0] = "#123456"
        jogo.move_left()
        self.assertEqual(jogo._tetri_col, 4)

    def test_game_over_ignora_comandos(self):
        jogo = JogoO()
        jogo._game_over = True
        jogo.move_left()
        jogo.move_right()
        jogo.move_down()
        jogo.drop()
        jogo.rotate()
        self.assertEqual((jogo._tetri_col, jogo._tetri_row), (4, 0))


class TestRotacao(unittest.TestCase):
    def test_gira_quando_cabe(self):
        jogo = JogoI()
        jogo.rotate()
        self.assertEqual(jogo.active_tetrimino.current_rotation, 1)

    def test_desfaz_giro_quando_nao_cabe(self):
        jogo = JogoI()
        jogo._grid[5][3] = "#123456"   # ocupa onde o I vertical ficaria
        jogo.rotate()
        self.assertEqual(jogo.active_tetrimino.current_rotation, 0)


class TestFixacao(unittest.TestCase):
    def test_drop_fixa_no_chao_e_cria_nova_peca(self):
        jogo = JogoO()
        jogo.drop()
        for c, r in [(4, 16), (5, 16), (4, 17), (5, 17)]:
            self.assertEqual(jogo._grid[c][r], "#ff0000")
        self.assertEqual((jogo._tetri_col, jogo._tetri_row), (4, 0))

    def test_move_down_no_chao_fixa(self):
        jogo = JogoO()
        for _ in range(16):
            jogo.move_down()
        self.assertIsNone(jogo._grid[4][17])
        jogo.move_down()
        self.assertEqual(jogo._grid[4][17], "#ff0000")

    def test_fim_de_jogo_quando_nova_peca_nao_cabe(self):
        jogo = JogoO()
        jogo._grid[4][0] = "#123456"
        jogo._new_tetrimino()
        self.assertTrue(jogo.game_over)

    def test_reset_desfaz_game_over(self):
        jogo = JogoO()
        jogo._game_over = True
        jogo._grid[0][17] = "#123456"
        jogo.reset()
        self.assertFalse(jogo.game_over)
        self.assertIsNone(jogo._grid[0][17])


class TestLinhas(unittest.TestCase):
    def test_sem_linhas_completas(self):
        self.assertEqual(JogoO()._clear_rows(), 0)

    def test_linha_removida_e_blocos_descem(self):
        jogo = JogoO()
        encher_linha(jogo, 17)
        jogo._grid[3][16] = "#123456"
        self.assertEqual(jogo._clear_rows(), 1)
        self.assertEqual(jogo._grid[3][17], "#123456")
        self.assertIsNone(jogo._grid[3][16])

    def test_linhas_consecutivas(self):
        jogo = JogoO()
        for r in (15, 16, 17):
            encher_linha(jogo, r)
        self.assertEqual(jogo._clear_rows(), 3)
        self.assertTrue(all(c is None for col in jogo._grid for c in col))

    def test_linhas_separadas(self):
        jogo = JogoO()
        encher_linha(jogo, 17)
        encher_linha(jogo, 15)
        jogo._grid[0][16] = "#111111"
        self.assertEqual(jogo._clear_rows(), 2)
        self.assertEqual(jogo._grid[0][17], "#111111")

    def test_lock_completa_linhas_no_jogo_real(self):
        jogo = JogoO()
        encher_linha(jogo, 17, exceto=(4, 5))
        encher_linha(jogo, 16, exceto=(4, 5))
        jogo.drop()   # O em col 4 completa as linhas 16 e 17
        self.assertTrue(all(jogo._grid[c][r] is None
                            for c in range(10) for r in (16, 17)))


if __name__ == "__main__":
    unittest.main()
