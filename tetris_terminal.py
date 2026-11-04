from tetris import Tetris


def colored_board(game: Tetris) -> str:
    RESET = "\033[0m"

    linhas = []
    borda = "+" + "---" * game.width + "+"
    linhas.append(borda)

    for linha in range(game.height):
        texto = "|"

        for coluna in range(game.width):
            cor = game.color_at(coluna, linha)

            if cor is not None:
                vermelho = int(cor[1:3], 16)
                verde = int(cor[3:5], 16)
                azul = int(cor[5:7], 16)

                ansi = f"\033[48;2;{vermelho};{verde};{azul}m"
                texto += f"{ansi}   {RESET}"
            else:
                texto += "   "

        texto += "|"
        linhas.append(texto)

    linhas.append(borda)

    return "\n".join(linhas)


class TetrisTerminal:

    def __init__(self):
        self.game = Tetris()

    def desenhar_tabuleiro(self):
        print(colored_board(self.game))

    def mostrar_menu(self):
        print("\n========== TETRIS ==========")
        print("A - Mover para esquerda")
        print("D - Mover para direita")
        print("S - Descer uma linha")
        print("W - Girar peça")
        print("X - Derrubar peça")
        print("R - Reiniciar jogo")
        print("Q - Sair")
        print("============================")

    def executar_comando(self, comando):
        if comando == "a":
            self.game.move_left()
        elif comando == "d":
            self.game.move_right()
        elif comando == "s":
            self.game.move_down()
        elif comando == "w":
            self.game.rotate()
        elif comando == "x":
            self.game.drop()
        elif comando == "r":
            self.game.reset()
        elif comando == "q":
            return False
        else:
            print("\nComando inválido!")

        return True

    def iniciar(self):
        continuar = True

        while continuar:
            self.desenhar_tabuleiro()

            if self.game.game_over:
                print("\n========== GAME OVER ==========")
                print("R - Jogar novamente")
                print("Q - Sair")
            else:
                self.mostrar_menu()

            comando = input("\nDigite seu comando: ").lower().strip()
            continuar = self.executar_comando(comando)

        print("\nObrigado por jogar Tetris!")


if __name__ == "__main__":
    jogo = TetrisTerminal()
    jogo.iniciar()