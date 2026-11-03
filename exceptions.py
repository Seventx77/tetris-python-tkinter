"""
Módulo exceptions.py

Define a hierarquia de exceções personalizadas para o jogo Tetris,
conforme especificado na arquitetura oficial do professor.
"""


class GamerError(Exception):
    """Exceção base de todos os erros do jogo."""
    pass


class InvalidBlockError(GamerError):
    """Lançada quando se tenta criar um bloco com coordenada negativa."""
    pass


class InvalidRotationError(GamerError):
    """Lançada quando se tenta criar um tetrimino com rotação inicial fora do intervalo 0 a 3."""
    pass
