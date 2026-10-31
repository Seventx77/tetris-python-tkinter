# 🧪 Planejamento de Testes do Projeto Tetris

Este documento estabelece o **plano estratégico de testes** para cada módulo do Tetris, seguindo a arquitetura em camadas orientada pelo professor.

> ⚠️ **Status Atual:** Nenhum teste executável foi implementado nesta etapa.  
> Conforme a metodologia de desenvolvimento, os testes serão criados progressivamente por cada integrante conforme seus respectivos módulos forem codificados.

---

## 📋 Matriz de Testes por Módulo e Integrante

### 1. Testes de Exceções (`exceptions.py`) — Integrante 1
- **Herança de Erros:**
  - Garantir que `GamerError` herde diretamente de `Exception`.
  - Garantir que `InvalidBlockError` e `InvalidRotationError` herdem de `GamerError`.
- **Tratamento Genérico:**
  - Garantir que capturar `GamerError` intercepte tanto erros de bloco quanto erros de rotação.

---

### 2. Testes da Classe Block (`block.py`) — Integrante 1
- **Criação e Coordenadas Válidas:**
  - Instanciar `Block(0, 0)`, `Block(5, 10)` e verificar se `block.x` e `block.y` retornam os inteiros esperados.
- **Validação de Coordenadas Negativas:**
  - Verificar se `Block(-1, 0)`, `Block(0, -1)` ou `Block(-2, -5)` disparam a exceção `InvalidBlockError`.
- **Imutabilidade:**
  - Garantir que tentativas de reatribuir `block.x = 10` gerem `AttributeError` (propriedades somente leitura).
- **Igualdade e Hash:**
  - Confirmar que `Block(2, 3) == Block(2, 3)` é `True`.
  - Confirmar que `Block(2, 3) == Block(3, 2)` é `False`.
  - Validar se instâncias de `Block` podem ser utilizadas em conjuntos (`set`) e tuplas imutáveis.

---

### 3. Testes dos Tetraminós e Rotações (`tetriminos.py`) — Integrante 2
- **Existência das 7 Subclasses:**
  - Instanciar `TetriminoI`, `TetriminoJ`, `TetriminoL`, `TetriminoO`, `TetriminoS`, `TetriminoT` e `TetriminoZ`.
  - Validar se todas herdam de `Tetrimino` e possuem as cores e `box_size` definidos.
- **Formas Iniciais e Quantidade de Blocos:**
  - Confirmar que cada tetraminó possui exatamente 4 instâncias de `Block` em qualquer rotação.
- **Fórmula de Rotação Horária:**
  - Validar a fórmula `(x, y) -> (box_size - 1 - y, x)` para 90°, 180° e 270°.
  - Confirmar que aplicar 4 rotações horárias consecutivas retorna a peça ao seu estado e orientação originais (ciclo completo de 360°).
- **Particularidade do TetriminoO:**
  - Confirmar que o quadrado 2x2 mantém a mesma disposição visual em todas as 4 rotações.

---

### 4. Testes do Modelo de Jogo e Regras (`tetris.py`) — Integrante 3
- **Dimensões do Tabuleiro:**
  - Confirmar que `game.width == 10` e `game.height == 18`.
  - Verificar se todas as posições iniciais em `_grid[col][row]` são inicializadas como `None`.
- **Geração e Posicionamento Inicial da Peça Ativa:**
  - Confirmar que `game.active_tetrimino` não é `None` após `game.reset()`.
  - Verificar se a peça nasce centralizada no topo (row = 0).
- **Movimentação Lateral e Limites:**
  - Mover a peça repetidamente para a esquerda até o limite e verificar se ela não ultrapassa a coluna 0.
  - Mover a peça repetidamente para a direita até o limite e verificar se ela não ultrapassa a coluna 9.
- **Descida, Colisão e Fixação (`_lock`):**
  - Fazer a peça descer até o fundo (linha 17) e validar se `_lock()` transfere seus blocos para `_grid`.
  - Confirmar que uma nova peça ativa é sorteada logo após a fixação da anterior.
- **Eliminação de Linhas Completas (`_clear_rows`):**
  - Preencher artificialmente uma linha inteira de 10 colunas na matriz e acionar `_clear_rows()`.
  - Confirmar que a linha foi removida, as linhas superiores desceram uma posição e o topo recebeu uma linha vazia.
- **Detecção de Game Over:**
  - Acumular blocos até o topo da matriz e validar se `game.game_over` torna-se `True` quando a nova peça não puder nascer.

---

### 5. Testes das Interfaces (`tetris_terminal.py` e `tetris_gui.py`) — Integrante 4
- **Interface de Terminal:**
  - Validar a função `colored_board(game)`: deve retornar uma string contendo exatamente 18 linhas renderizadas com delimitadores.
  - Verificar se os comandos `'a'`, `'d'`, `'s'`, `'w'`, `'x'` delegam as chamadas aos respectivos métodos de `Tetris`.
- **Interface Gráfica Tkinter:**
  - Validar a instanciação de `TetrisApp` sem erros de importação.
  - Verificar se `restart()` limpa o Canvas e reinicia o estado do jogo.
  - Verificar se `schedule_fall()` e `fall()` manipulam corretamente o agendamento de 500ms via `after`.
