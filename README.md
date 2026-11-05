# 🕹️ Tetris em Python + Tkinter

Projeto acadêmico colaborativo de implementação do clássico jogo **Tetris**, desenvolvido em linguagem **Python** com arquitetura orientada a objetos desacoplada, oferecendo duas interfaces de usuário: **Interface Gráfica (Tkinter)** e **Interface Textual (Terminal/Console)**.

---

## 🎯 1. Objetivo Acadêmico

Este projeto tem finalidade exclusivamente educacional e acadêmica. O objetivo é aplicar, de forma prática e modular, conceitos essenciais de **Programação Orientada a Objetos (POO)** e boas práticas de engenharia de software:

- **Encapsulamento e Imutabilidade:** Criação de componentes fundamentais imutáveis (`Block`).
- **Herança e Polimorfismo:** Classe base abstrata (`Tetrimino`) e especialização nas 7 peças clássicas (I, J, L, O, S, T, Z).
- **Tratamento de Exceções Personalizadas:** Hierarquia estruturada (`GamerError`, `InvalidBlockError`, `InvalidRotationError`).
- **Separação Rígida entre Modelo e Visão:** O motor de regras (`Tetris`) não possui qualquer dependência de código visual ou de entrada e saída (`print`/`input`), podendo ser consumido igualmente por interfaces gráficas ou de console.
- **Trabalho Colaborativo:** Controle de versão distribuído via Git e GitHub, organização modular de responsabilidades e revisão de código.

---

## 🛠️ 2. Tecnologias Utilizadas

- **Linguagem:** Python 3 (Python 3.10 ou superior recomendado; compatível com Python 3.8+)
- **Interface Gráfica:** Tkinter (biblioteca gráfica padrão do Python)
- **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)
- **Controle de Versão:** Git e GitHub

---

## 🏛️ 3. Arquitetura do Sistema e Organização dos Módulos

O projeto adota uma arquitetura em camadas totalmente desacoplada:

```text
┌─────────────────────────────────────────────────────────────────┐
│                     CAMADA DE APRESENTAÇÃO                      │
│   tetris_terminal.py (Console)      tetris_gui.py (Tkinter)     │
└────────────────────────────────┬────────────────────────────────┘
                                 │ consome (width, height, color_at, comandos)
┌────────────────────────────────▼────────────────────────────────┐
│                   CAMADA DE NEGÓCIO / MODELO                    │
│                            tetris.py                            │
│           (Tabuleiro 10x18, colisões, linhas, controle)         │
└────────────────────────────────┬────────────────────────────────┘
                                 │ utiliza
┌────────────────────────────────▼────────────────────────────────┐
│                     CAMADA DE PEÇAS E FORMAS                    │
│                         tetriminos.py                           │
│        (Tetrimino abstrato, 7 subclasses, 4 rotações)           │
└────────────────────────────────┬────────────────────────────────┘
                                 │ composto por
┌────────────────────────────────▼────────────────────────────────┐
│                      CAMADA BASE / DOMÍNIO                      │
│             block.py (Bloco imutável com coords x, y)           │
│             exceptions.py (Hierarquia oficial GamerError)       │
└─────────────────────────────────────────────────────────────────┘
```

### Estrutura de Arquivos:

- **`exceptions.py`:** Hierarquia oficial de exceções (`GamerError`, `InvalidBlockError`, `InvalidRotationError`).
- **`block.py`:** Classe `Block` imutável, representando cada célula de um tetraminó com coordenadas `(x, y)` e validação de coordenadas negativas.
- **`tetriminos.py`:** Classe abstrata `Tetrimino` e as 7 subclasses (`TetriminoI`, `TetriminoJ`, `TetriminoL`, `TetriminoO`, `TetriminoS`, `TetriminoT`, `TetriminoZ`), com pré-cálculo das 4 rotações horárias e cores correspondentes.
- **`tetris.py`:** Motor do jogo contendo o tabuleiro $10 \times 18$ (`_grid[coluna][linha]`), controle da peça ativa, colisões laterais e de fundo, fixação (`_lock`), remoção de linhas completas (`_clear_rows`) e detecção de Game Over.
- **`tetris_terminal.py`:** Interface em modo texto exibindo o tabuleiro com caracteres formatados em cores ANSI e controle via teclado.
- **`tetris_gui.py`:** Interface gráfica nativa em Tkinter com renderização via `Canvas`, queda automática com temporizador de 500 ms (`after`), painel de status e botão de reinício.
- **`tests/`:** Suíte de testes automatizados unitários do motor e da integração dos módulos.

---

## 👥 4. Divisão Oficial da Equipe

O projeto foi dividido em módulos específicos entre os quatro integrantes:

- **Robert:** `block.py` e `tetriminos.py`
- **Romerson:** `tetris_gui.py` e `tetris_terminal.py`
- **Josue:** `tetris.py`
- **Lucas:** `exceptions.py`

---

## ⚙️ 5. Requisitos para Execução

- Ter o **Python 3.8+** instalado (recomendado Python 3.10 ou superior).
- O **Tkinter** deve estar disponível no ambiente:
  - No Windows e macOS, o Tkinter é instalado por padrão com o instalador oficial do Python.
  - Em sistemas Linux (Debian/Ubuntu), caso necessário, instale com:
    ```bash
    sudo apt install python3-tk
    ```

Para verificar se o Tkinter está ativo, execute:
```bash
python -c "import tkinter; print('Tkinter disponível')"
```

---

## 🚀 6. Como Executar o Jogo

### A. Executando a Interface Gráfica (Tkinter)

A interface gráfica é a forma visual padrão de jogar o Tetris:

```bash
python tetris_gui.py
```

**Controles na Interface Gráfica:**
- `←` (Seta Esquerda): Mover para a esquerda
- `→` (Seta Direita): Mover para a direita
- `↑` (Seta para Cima): Girar peça no sentido horário
- `↓` (Seta para Baixo): Acelerar descida (soft drop)
- `Espaço`: Derrubar a peça diretamente ao fundo (hard drop)
- Botão **REINICIAR**: Iniciar uma nova partida a qualquer momento ou após o Game Over.

---

### B. Executando a Interface de Console (Terminal)

Para jogar em modo texto no terminal com suporte a cores ANSI:

```bash
python tetris_terminal.py
```

**Comandos do Terminal:**
- `a`: Mover para a esquerda
- `d`: Mover para a direita
- `s`: Descer uma linha
- `w`: Girar a peça
- `x`: Derrubar a peça (drop)
- `r`: Reiniciar a partida
- `q`: Sair do jogo

---

## 🧪 7. Como Executar os Testes Automatizados

O projeto utiliza a biblioteca nativa `unittest` do Python.

Para executar a suíte de testes completa, execute no terminal a partir da raiz do projeto:

```bash
python -m unittest discover -s tests
```

### Resultados Reais dos Testes:
- **Testes Executados:** 21 testes unitários em `tests/test_tetris.py`.
- **Status:** **21 testes aprovados (100% de sucesso)**.
- **Cobertura avaliada:**
  - Inicialização do tabuleiro ($10 \times 18$) e centralização no topo.
  - Verificação de limites laterais e inferiores (`_tetri_fits`).
  - Colisões com blocos já fixados.
  - Movimentação lateral e descida.
  - Rotação com reversão automática caso não caiba.
  - Fixação de peças no tabuleiro (`_lock`).
  - Remoção de linhas completas (simples, consecutivas e separadas).
  - Detecção de fim de jogo (Game Over) e reinicialização (`reset()`).
  - Validação de hierarquia de exceções (`GamerError`) e imutabilidade do bloco.

---

## ⚠️ 8. Limitações Conhecidas

1. **Ambiente Gráfico:** A execução do módulo `tetris_gui.py` necessita de um servidor gráfico / display ativo (ambiente desktop tradicional).
2. **Cores no Terminal:** A interface `tetris_terminal.py` utiliza códigos de escape ANSI TrueColor (24-bit); terminais legados sem suporte a ANSI exibirão os caracteres sem o realce colorido de fundo.
