"""
MÓDULO: exceptions.py
RESPONSÁVEL: Integrante 1 (Exceções e Bloco Imutável)
DESCRIÇÃO:
    Este módulo define a hierarquia de exceções personalizadas para o jogo Tetris,
    conforme a arquitetura oficial e especificações do professor.

HIERARQUIA OFICIAL DO PROFESSOR (UML):
    Exception
       └── GamerError               - Classe base de erro do jogo
             ├── InvalidBlockError   - Lançada se coordenadas x ou y forem negativas
             └── InvalidRotationError - Lançada se a rotação inicial for inválida

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    A PROGRAMAÇÃO AINDA NÃO COMEÇOU.
    Este arquivo contém apenas comentários explicativos e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DAS CLASSES DE EXCEÇÃO (INTEGRANTE 1)
# ==============================================================================

# TODO: Definir a classe base de exceção conforme o diagrama UML:
#       class GamerError(Exception):
#           """Classe base para todas as exceções do jogo Tetris."""
#           pass
#       (Dica: pode-se disponibilizar GameError = GamerError como alias).

# TODO: Definir a exceção InvalidBlockError:
#       class InvalidBlockError(GamerError):
#           """
#           Lançada na tentativa de criar ou manipular um bloco com coordenadas negativas
#           (x < 0 ou y < 0).
#           """
#           pass

# TODO: Definir a exceção InvalidRotationError:
#       class InvalidRotationError(GamerError):
#           """
#           Lançada ao tentar instanciar um tetraminó com rotação inválida
#           (fora do intervalo 0 a 3).
#           """
#           pass
