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

import tkinter as tk

# Configurações do tabuleiro
COLUNAS = 10
LINHAS = 18
TAMANHO_DA_CELULA = 30

LARGURA = COLUNAS * TAMANHO_DA_CELULA
ALTURA = LINHAS * TAMANHO_DA_CELULA




class TetrisApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tetris")
        self.resizable(False, False)

        #posição inicial das peças
        self.peca_linha = 0
        self.peca_coluna = 0

        #peça para teste
        self.peca = [
            [1, 1, 1],
            [1, 0, 0]
        ]

        #criando a interface
        self.criar_interface()
        #desenhar o tabuleiro
        self.atualizar_tela()
        #queda automática
        self.after(500, self.queda_automatica)

    def reiniciar_jogo(self):

        #volta a peça para a posição inicial
        self.peca_linha = 0
        self.peca_coluna = 0

        #restaura a peça original
        self.peca = [
            [1, 1, 1],
            [1, 0, 0]
        ]

        #zera a pontuação
        self.valor_score.config(text="0")

        #atualiza o tabuleiro
        self.atualizar_tela()

    def criar_interface(self):
        #canva no tabuleiro
        self.canvas = tk.Canvas(
            self, 
            width=LARGURA,
            height=ALTURA,
            bg="black"
        ) 
        self.canvas.pack(side="left", padx=10, pady=10)

        #painel lateral
        self.painel = tk.Frame(self, bg="black")
        self.painel.pack(side="right", padx=20)

        #carta da pontuação
        card_score = tk.Frame(
            self.painel,
            bg="#1e1e2e", 
            padx=15,
            pady=10
        )
        card_score.pack(fill="x", pady=10)

        titulo_score = tk.Label(
            card_score,
            text="SCORE",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1e1e2e"
        )
        titulo_score.pack(pady=5)

        self.valor_score =tk.Label(
            card_score,
            text="0",
            font=("Arial", 26, "bold"),
            fg="#00ff99",
            bg="#1e1e2e"
        )
        self.valor_score.pack(pady=5)
        #título do nivel
        titulo_nivel = tk.Label(
            self.painel,
            text="NÍVEL",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="black"
        )
        titulo_nivel.pack(pady=10)
        
        #valor do nivel
        self.valor_nivel = tk.Label(
            self.painel,
            text="1",
            font=("Arial", 22, "bold"),
            fg="white",
            bg="black"
        )
        self.valor_nivel.pack(pady=5)

        #titulo da próxima peça
        titulo_proxima = tk.Label(
            self.painel,
            text="PRÓXIMA PEÇA",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="black"
        )
        titulo_proxima.pack(pady=20)

        #Canvas da próxima peça
        self.canvas_proxima = tk.Canvas(
            self.painel,
            width=120,
            height=120,
            bg="black",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.canvas_proxima.pack()

        # Botão para reiniciar o jogo
        self.botao_restart = tk.Button(
        self.painel,
        text="RESTART",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#e74c3c",
        activebackground="#c0392b",
        activeforeground="white",
        width=15,
        command=self.reiniciar_jogo
    )
        self.botao_restart.pack(pady=25)

        #Controles do jogo
        self.bind("<Right>", self.mover_direita)
        self.bind("<Left>", self.mover_esquerda)
        self.bind("<Down>", self.mover_baixo)
        self.bind("<Up>", self.rotacionar)

    def desenhar_tabuleiro(self):

        for linha in range(LINHAS):
            for coluna in range(COLUNAS):

                x1 = coluna * TAMANHO_DA_CELULA
                y1 = linha * TAMANHO_DA_CELULA

                x2 = x1 + TAMANHO_DA_CELULA
                y2 = y1 + TAMANHO_DA_CELULA

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    outline="gray"
                )

    def desenhar_bloco(self, linha, coluna, cor):

        x1 = coluna * TAMANHO_DA_CELULA
        y1 = linha * TAMANHO_DA_CELULA

        x2 = x1 + TAMANHO_DA_CELULA
        y2 = y1 + TAMANHO_DA_CELULA

        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=cor,
            outline="white"
        )

    def desenhar_peca(self):

        for linha in range(len(self.peca)):
            for coluna in range(len(self.peca[linha])):

                if self.peca[linha][coluna] == 1:

                    self.desenhar_bloco(
                        self.peca_linha + linha,
                        self.peca_coluna + coluna,
                        "blue"
                    )

    def atualizar_tela(self):

        self.canvas.delete("all")

        self.desenhar_tabuleiro()
        self.desenhar_peca()

    def mover_direita(self, event):

        largura_peca = len(self.peca[0])

        if self.peca_coluna < COLUNAS - largura_peca:
            self.peca_coluna += 1

        self.atualizar_tela()

    def mover_esquerda(self, event):

        if self.peca_coluna > 0:
            self.peca_coluna -= 1

        self.atualizar_tela()

    def mover_baixo(self, event):

        altura_peca = len(self.peca)

        if self.peca_linha < LINHAS - altura_peca:
            self.peca_linha += 1

        self.atualizar_tela()

    def queda_automatica(self):

        if self.peca_linha < LINHAS - len(self.peca):
            self.peca_linha += 1

        self.atualizar_tela()

        self.after(500, self.queda_automatica)

    def rotacionar(self, event):

        nova_peca = [
            list(linha)
            for linha in zip(*self.peca[::-1])
        ]

        largura = len(nova_peca[0])
        altura = len(nova_peca)

        if (self.peca_coluna + largura <= COLUNAS and
                self.peca_linha + altura <= LINHAS):

            self.peca = nova_peca

        self.atualizar_tela()


#inicialização do jogo
if __name__ == "__main__":
    jogo = TetrisApp()
    jogo.mainloop()
        
