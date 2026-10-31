"""
MÓDULO: tetris_terminal.py
RESPONSÁVEL: Integrante 4 (Interfaces: Terminal e Gráfica)
DESCRIÇÃO:
    Este módulo implementa a interface em modo texto (terminal/console) para o
    jogo Tetris, conforme a especificação do professor.

REQUISITOS DO PROFESSOR:
    - As interfaces NÃO implementam regra de jogo nenhuma.
    - Mostram o estado do jogo usando apenas width, height, color_at e game_over.
    - Função: colored_board(game: Tetris) -> str (pinta cada bloco com a cor da peça usando códigos ANSI).
    - Lê um comando por vez:
        'a' / 'd': esquerda / direita
        's': descer
        'w': girar
        'x': derrubar
        'q': sair

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    A PROGRAMAÇÃO AINDA NÃO COMEÇOU.
    Este arquivo contém apenas comentários explicativos e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DA INTERFACE TEXTUAL (INTEGRANTE 4)
# ==============================================================================

# TODO: Importar o modelo central do Tetris:
#       from tetris import Tetris

# TODO: Planejar a função de renderização textual com cores ANSI:
#       def colored_board(game: Tetris) -> str:
#           """
#           Gera e retorna a representação em string do estado do tabuleiro:
#           - Itera sobre as linhas de 0 até game.height - 1 e colunas de 0 até game.width - 1.
#           - Consulta color = game.color_at(c, r).
#           - Se color for None, exibe célula vazia (ex: ' . ').
#           - Se houver cor, renderiza o bloco usando códigos de cor ANSI de acordo com color.
#           - Inclui bordas laterais e inferiores.
#           """
#           pass

# TODO: Planejar o laço principal de jogo no console:
#       def main():
#           """
#           1. Instancia o jogo: game = Tetris()
#           2. Enquanto not game.game_over:
#              a. Imprime colored_board(game).
#              b. Lê a tecla via input("Comando: ").
#              c. Repassa o comando para game.move_left(), move_right(), move_down(),
#                 rotate(), drop(), ou sai do loop se 'q'.
#           3. Exibe mensagem de Fim de Jogo quando game.game_over for True.
#           """
#           pass

# TODO: Ponto de entrada padrão:
#       if __name__ == "__main__":
#           main()
