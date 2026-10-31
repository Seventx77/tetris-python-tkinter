"""
MÓDULO: tetris_gui.py
RESPONSÁVEL: Integrante 4 (Interfaces: Terminal e Gráfica)
DESCRIÇÃO:
    Este módulo implementa a interface gráfica (GUI) baseada em Tkinter para o
    jogo Tetris, conforme o diagrama UML e os requisitos do professor.

REQUISITOS DO PROFESSOR:
    - As interfaces NÃO implementam regra de jogo nenhuma.
    - Classe TetrisApp herdando de tk.Tk.
    - Atributos previstos:
        * game: Tetris
        * after_id: str | None
        * canvas: tk.Canvas
        * status: tk.Label
    - Métodos previstos:
        * play(move: Callable[[], None])
        * schedule_fall()
        * fall()
        * restart()
        * draw()
    - Desenha o tabuleiro em um Canvas (usando width, height, color_at).
    - Faz a peça cair sozinha a cada 500 ms (com root.after).
    - Botão "Reiniciar" (chama restart).
    - Controles:
        * Setas ← / → : movem (esquerda / direita)
        * Seta ↑      : gira
        * Seta ↓      : desce
        * Espaço      : derruba (drop)

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    A PROGRAMAÇÃO AINDA NÃO COMEÇOU.
    Este arquivo contém apenas comentários explicativos e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DA INTERFACE GRÁFICA TKINTER (INTEGRANTE 4)
# ==============================================================================

# TODO: Importar recursos necessários:
#       import tkinter as tk
#       from typing import Callable, Optional
#       from tetris import Tetris

# TODO: Planejar a classe TetrisApp herdando de tk.Tk:
#       class TetrisApp(tk.Tk):
#           CELL_SIZE = 30  # Tamanho em pixels de cada célula no Canvas
#
#           def __init__(self):
#               # super().__init__()
#               # self.title("Tetris - Python Tkinter")
#               # self.game = Tetris()
#               # self.after_id: Optional[str] = None
#               # Criar widgets:
#               #   self.canvas = tk.Canvas(...)
#               #   self.status = tk.Label(...)
#               #   Botão "Reiniciar" acionando self.restart
#               # Vincular eventos de teclado:
#               #   <Left>  -> self.play(self.game.move_left)
#               #   <Right> -> self.play(self.game.move_right)
#               #   <Up>    -> self.play(self.game.rotate)
#               #   <Down>  -> self.play(self.game.move_down)
#               #   <space> -> self.play(self.game.drop)
#               # Iniciar a queda automática: self.schedule_fall()
#               # Desenhar tela inicial: self.draw()
#               pass
#
#           def play(self, move: Callable[[], None]):
#               """
#               Executa a função de movimento recebida no modelo (ex: self.game.move_left)
#               e redesenha a tela chamando self.draw().
#               """
#               pass
#
#           def schedule_fall(self):
#               """Agenda a próxima chamada de self.fall() para daqui a 500ms usando self.after()."""
#               pass
#
#           def fall(self):
#               """
#               Executa a descida periódica chamando self.game.move_down(),
#               redesenha o tabuleiro (self.draw()) e, se not self.game.game_over,
#               reagenda a próxima queda com self.schedule_fall().
#               """
#               pass
#
#           def restart(self):
#               """
#               Reinicia o jogo:
#               - Cancela agendamento anterior se self.after_id existir (self.after_cancel).
#               - Chama self.game.reset().
#               - Reagenda a queda com self.schedule_fall().
#               - Redesenha com self.draw().
#               """
#               pass
#
#           def draw(self):
#               """
#               Limpa o Canvas e redesenha o tabuleiro:
#               - Varre colunas de 0 a self.game.width - 1 e linhas de 0 a self.game.height - 1.
#               - Para cada célula, obtém color = self.game.color_at(col, row).
#               - Se houver cor, desenha o retângulo preenchido na célula correspondente.
#               - Desenha as linhas da grade do tabuleiro.
#               - Se self.game.game_over for True:
#                   Exibe aviso visual de Fim de Jogo no label self.status ou no Canvas.
#               """
#               pass

# TODO: Ponto de entrada padrão:
#       if __name__ == "__main__":
#           app = TetrisApp()
#           app.mainloop()
