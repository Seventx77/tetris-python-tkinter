"""
MÓDULO: parte2_pecas.py
RESPONSÁVEL: Integrante 2 (Peças e Movimentação)
DESCRIÇÃO:
    Este módulo será responsável pela definição das 7 peças clássicas do Tetris
    (tetraminós: I, J, L, O, S, T, Z), suas cores correspondentes, suas
    coordenadas relativas, sistemas de rotação e funções para movimentar
    a peça ativa (mover para esquerda, direita e acelerar descida).

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    Este arquivo contém apenas a estrutura inicial planejada e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DE RESPONSABILIDADES (INTEGRANTE 2)
# ==============================================================================
# TODO: Definir as 7 formas clássicas do Tetris (I, J, L, O, S, T, Z):
#       - Decidir a representação (ex: matrizes 3x3 / 4x4, ou lista de coordenadas relativas (x, y)).
#       - Definir as cores oficiais ou personalizadas para cada tipo de peça.

# TODO: Planejar a representação da peça ativa:
#       - Tipo da peça atual
#       - Posição atual no tabuleiro (linha, coluna de referência)
#       - Estado atual de rotação (índice 0 a 3, ou ângulo)
#       - Cor associada

# TODO: Planejar as funções/métodos de geração e movimentação:
#       - Função para sortear uma nova peça aleatória (ex: usando random.choice)
#       - Função para mover para a esquerda (ex: coluna -= 1)
#       - Função para mover para a direita (ex: coluna += 1)
#       - Função para descer um nível (ex: linha += 1)
#       - Função/lógica para rotacionar a peça (girar matriz no sentido horário)

# TODO: Alinhar com os Integrantes 3 e 4:
#       - O Integrante 3 (Colisões) precisará testar se o movimento ou rotação é válido
#         antes de confirmar a alteração de posição/estado da peça.
#       - O Integrante 4 (Integração) precisará disparar os movimentos através dos
#         eventos de teclado (setas do teclado, espaço, etc.).
