"""
MÓDULO: parte1_tabuleiro.py
RESPONSÁVEL: Integrante 1 (Tabuleiro e Interface Visual)
DESCRIÇÃO:
    Este módulo será responsável pela criação da janela gráfica (Tkinter),
    do Canvas onde o jogo é desenhado, da definição das dimensões do tabuleiro
    (largura, altura e tamanho das células em pixels), e da renderização
    da grade e dos elementos estáticos e dinâmicos na tela.

ATENÇÃO:
    NENHUM CÓDIGO FUNCIONAL FOI IMPLEMENTADO AINDA.
    Este arquivo contém apenas a estrutura inicial planejada e marcadores TODO.
"""

# ==============================================================================
# PLANEJAMENTO DE RESPONSABILIDADES (INTEGRANTE 1)
# ==============================================================================
# TODO: Importar as bibliotecas necessárias do Tkinter (ex: tkinter as tk).
# TODO: Definir constantes visuais recomendadas:
#       - LARGURA_TABULEIRO (ex: 10 colunas)
#       - ALTURA_TABULEIRO (ex: 20 linhas)
#       - TAMANHO_CELULA (tamanho em pixels de cada bloco)
#       - Cores de fundo e linhas da grade

# TODO: Planejar a estrutura da interface gráfica:
#       - Criação da janela principal (tk.Tk ou Toplevel)
#       - Configuração de título e tamanho fixo
#       - Criação do Canvas para renderizar a área jogável
#       - Painel lateral para pontuação, nível e próxima peça (a combinar com Integrante 4)

# TODO: Planejar as funções/métodos de desenho:
#       - Função para desenhar a grade do tabuleiro (linhas horizontais e verticais)
#       - Função para desenhar uma célula/bloco individual dada a coordenada (linha, coluna) e cor
#       - Função para redesenhar/limpar o tabuleiro a cada quadro (tick)
#       - Função para renderizar blocos fixados recebidos da estrutura do jogo

# TODO: Alinhar com o Integrante 4 (Integração):
#       - Como este módulo fornecerá o Canvas ou a Janela para o laço principal do jogo.
#       - Qual será o formato de dados do tabuleiro (ex: matriz de cores/ocupação).
