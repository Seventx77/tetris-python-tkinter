"""
MÓDULO: parte3_colisoes.py
RESPONSÁVEL: Integrante 3 (Colisões e Eliminação de Linhas)
DESCRIÇÃO:
    Este módulo será responsável pelas regras mais críticas e de maior
    complexidade lógica do jogo:
    1. Detecção de limites (paredes esquerda, direita e chão do tabuleiro).
    2. Detecção de sobreposição com blocos já fixados (colisão de peças).
    3. Fixação da peça no tabuleiro quando ela não puder mais descer (lock).
    4. Verificação e identificação de linhas horizontais completamente cheias.
    5. Remoção dessas linhas, descida de todos os blocos superiores e contagem
       de linhas eliminadas para cálculo de pontos.

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    Este arquivo contém apenas a estrutura inicial planejada e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DE RESPONSABILIDADES (INTEGRANTE 3)
# ==============================================================================
# TODO: Planejar a validação de posições e movimentos (Detecção de Colisões):
#       - Função para verificar se uma peça em determinada coordenada (linha, coluna)
#         e rotação está dentro dos limites do tabuleiro:
#           * Coluna >= 0 e Coluna < LARGURA
#           * Linha < ALTURA
#       - Função para verificar se algum bloco da peça colide com blocos já fixados
#         no tabuleiro (consultando a matriz do tabuleiro).
#       - Função combinada `posicao_valida(peca, tabuleiro, nova_linha, nova_coluna)`:
#         retorna True se o movimento/rotação pode acontecer, ou False caso contrário.

# TODO: Planejar a fixação da peça (Lockdown):
#       - Função para copiar os blocos da peça ativa para a matriz permanente do tabuleiro
#         assim que ela atingir o chão ou colidir com blocos inferiores.

# TODO: Planejar a eliminação de linhas completas:
#       - Função para varrer o tabuleiro e identificar linhas cujas colunas estão todas ocupadas.
#       - Função para remover as linhas preenchidas da matriz do tabuleiro.
#       - Função para inserir novas linhas vazias no topo do tabuleiro, descendo as restantes.
#       - Retornar o número de linhas eliminadas (1, 2, 3 ou 4 - Tetris) para que o
#         Integrante 4 possa atualizar a pontuação do jogador.

# TODO: Planejar a detecção de Game Over preliminar:
#       - Verificar se a nova peça sorteada nasce em uma posição já ocupada no topo.

# TODO: Alinhar com os Integrantes 1, 2 e 4:
#       - Acertar com o Integrante 1 como a matriz do tabuleiro armazena os dados
#         (ex: matriz de inteiros, None para vazio e hex/string para cor).
#       - Acertar com o Integrante 2 como obter as coordenadas absolutas de cada bloco da peça.
#       - Acertar com o Integrante 4 quando disparar a verificação de linhas e o retorno de pontos.
