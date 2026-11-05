import tkinter as tk
from typing import Callable
from tetris import Tetris


class TetrisApp(tk.Tk):

    CELL_SIZE = 30

    def __init__(self):
        super().__init__()

        self.title("Tetris")
        self.resizable(False, False)

        self.game = Tetris()
        self.after_id = None

        self.canvas = tk.Canvas(
            self,
            width=self.game.width * self.CELL_SIZE,
            height=self.game.height * self.CELL_SIZE,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(padx=15, pady=10)

        self.status = tk.Label(
            self,
            text="Use as setas para movimentar e ESPAÇO para derrubar",
            font=("Arial", 10),
            bg="#222222",
            fg="white",
            pady=8
        )
        self.status.pack(fill="x", padx=15)

        self.botao_restart = tk.Button(
            self,
            text="REINICIAR",
            font=("Arial", 11, "bold"),
            command=self.restart
        )
        self.botao_restart.pack(pady=12)

        self.bind_all("<Left>", lambda event: self.play(self.game.move_left))
        self.bind_all("<Right>", lambda event: self.play(self.game.move_right))
        self.bind_all("<Up>", lambda event: self.play(self.game.rotate))
        self.bind_all("<Down>", lambda event: self.play(self.game.move_down))
        self.bind_all("<space>", lambda event: self.play(self.game.drop))

        self.draw()
        self.schedule_fall()

    def play(self, move: Callable[[], None]):
        if self.game.game_over:
            return

        move()
        self.draw()

        if self.game.game_over and self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

    def schedule_fall(self):
        if not self.game.game_over and self.after_id is None:
            self.after_id = self.after(500, self.fall)

    def fall(self):
        self.after_id = None

        if not self.game.game_over:
            self.game.move_down()
            self.draw()

            if not self.game.game_over:
                self.schedule_fall()

    def restart(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
            self.after_id = None

        self.game.reset()
        self.status.config(
            text="Use as setas para movimentar e ESPAÇO para derrubar"
        )

        self.draw()
        self.schedule_fall()

    def draw(self):
        self.canvas.delete("all")

        for linha in range(self.game.height):
            for coluna in range(self.game.width):

                x1 = coluna * self.CELL_SIZE
                y1 = linha * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE

                cor = self.game.color_at(coluna, linha)

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=cor if cor is not None else "#111111",
                    outline="#444444"
                )

        if self.game.game_over:
            self.status.config(text="FIM DE JOGO! Clique em REINICIAR.")
        else:
            self.status.config(
                text="← → Movimentar | ↑ Girar | ↓ Descer | ESPAÇO Derrubar"
            )


if __name__ == "__main__":
    app = TetrisApp()
    app.mainloop()