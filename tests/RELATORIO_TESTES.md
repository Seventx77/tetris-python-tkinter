# 📊 Relatório de Testes e Validação do Projeto Tetris

Este documento consolida os resultados reais de testes e validação do projeto acadêmico **Tetris em Python + Tkinter**, cobrindo o modelo de regras, as exceções, os blocos, as peças e as interfaces de usuário.

---

## 🖥️ 1. Ambiente de Execução e Versões Identificadas

- **Sistema Operacional:** Microsoft Windows NT 10.0.26200.0 (Windows 11)
- **Interpretador Python:** Python 3.14.7
- **Biblioteca Gráfica:** Tkinter (módulo padrão ativo)
- **Estrutura de Testes:** Python `unittest` (módulo padrão)
- **Branch Validada:** `feature/arquitetura-professor`

---

## 🎯 2. Objetivo da Validação

Verificar a conformidade do projeto com as regras oficiais do professor, garantindo:
1. O funcionamento correto e a herança das classes de exceção (`GamerError`).
2. A imutabilidade e integridade da classe `Block`.
3. A inicialização, rotação e silenciamento de importação das 7 peças em `tetriminos.py`.
4. A lógica do motor de jogo `Tetris` (tabuleiro $10 \times 18$, colisões, fixação, linhas cheias e Game Over).
5. A integração e a operacionalidade das interfaces de Terminal e Tkinter.

---

## 📋 3. Matriz de Resultados das Verificações

| Categoria / Componente | Descrição da Verificação | Comando / Método de Teste | Resultado |
| :--- | :--- | :--- | :--- |
| **Exceções: Herança** | `GamerError` herda de `Exception`; `InvalidBlockError` e `InvalidRotationError` herdam de `GamerError` | `issubclass(...)` via Python | **Aprovado** |
| **Exceções: Polimorfismo** | Captura de `InvalidBlockError` e `InvalidRotationError` por bloco `except GamerError` | Script de teste unitário | **Aprovado** |
| **Block: Coordenadas** | `Block(x, y)` armazena coordenadas positivas corretamente | Instanciação e leitura de propriedades | **Aprovado** |
| **Block: Validação Negativa** | `Block(-1, y)` e `Block(x, -1)` disparam `InvalidBlockError` | Teste com bloco `try/except` | **Aprovado** |
| **Block: Imutabilidade** | Atribuições `b.x = 10` ou `b.y = 10` levantam `AttributeError` | Teste de reatribuição de propriedade | **Aprovado** |
| **Block: Igualdade e Hash** | Dois blocos com mesmo `(x, y)` são iguais e geram mesmo hash | `b1 == b2` e inserção em `set` | **Aprovado** |
| **Tetrimino: Rotação Inválida** | Inicialização com `initial_rotation < 0` ou `> 3` levanta `InvalidRotationError` | `TetriminoI(-1)` e `TetriminoT(4)` | **Aprovado** |
| **Tetrimino: Importação Limpa** | `import tetriminos` não imprime demonstrações no stdout | `python -c "import tetriminos"` | **Aprovado** |
| **Tetris: Dimensões** | Tabuleiro inicializa com 10 colunas e 18 linhas | `TestInicio.test_tamanho_do_tabuleiro` | **Aprovado** |
| **Tetris: Posição Inicial** | Peça nasce centralizada no topo: `(4, 0)` para caixa 2 | `TestInicio.test_peca_nasce_centralizada_no_topo` | **Aprovado** |
| **Tetris: Paredes e Chão** | `_tetri_fits` barra colunas fora de $[0, 9]$ e linhas fora de $[0, 17]$ | `TestCabe.test_paredes_e_chao` | **Aprovado** |
| **Tetris: Colisão de Blocos** | `_tetri_fits` barra sobreposição com blocos já preenchidos | `TestCabe.test_bloco_fixado` | **Aprovado** |
| **Tetris: Movimentação** | Peça move lateralmente e para na parede; desce com `move_down` | `TestMovimentos` (4 testes) | **Aprovado** |
| **Tetris: Fim de Jogo e Bloqueio** | Comandos `move_left`, `move_right`, `down`, `drop`, `rotate` são ignorados em Game Over | `TestMovimentos.test_game_over_ignora_comandos` | **Aprovado** |
| **Tetris: Rotação com Reversão** | Gira 90° horário se couber; desfaz o giro se houver colisão | `TestRotacao` (2 testes) | **Aprovado** |
| **Tetris: Fixação (`_lock`)** | Peça no fundo é fixada em `_grid` e gera nova peça ativa | `TestFixacao` (3 testes) | **Aprovado** |
| **Tetris: Limpeza de Linhas** | Linhas cheias (simples, consecutivas e alternadas) são removidas e blocos descem | `TestLinhas` (4 testes) | **Aprovado** |
| **Tetris: Reinício (`reset`)** | Limpa todo o tabuleiro, desfaz o Game Over e sorteia nova peça | `TestFixacao.test_reset_desfaz_game_over` | **Aprovado** |
| **Terminal: Módulo e ANSI** | `colored_board(game)` gera string do tabuleiro com escape ANSI | `python tetris_terminal.py` (simulado) | **Aprovado** |
| **Terminal: Entrada Interativa** | Processamento de teclas `a, d, s, w, x, r, q` em sessão interativa | Execução de teste automatizado via pipe | **Aprovado** |
| **Tkinter: Disponibilidade** | Biblioteca `tkinter` funcional no interpretador Python | `python -c "import tkinter; ..."` | **Aprovado** |
| **Tkinter: Ciclo de Vida do App** | `TetrisApp` instancia, cria Canvas $300 \times 540$, executa `update()`, `play()`, `restart()` e `destroy()` | Script de automação do ciclo de vida | **Aprovado** |
| **Tkinter: Inspeção Visual em Tela** | Verificação visual humana dos retângulos e cores em janela desktop aberta | Visualização ocular interativa do usuário | **Não foi possível verificar** *(requer display físico ativo)* |

---

## 🔬 4. Execução da Suíte Automatizada Principal

Comando executado:
```bash
python -m unittest discover -s tests
```

### Saída Real do Terminal:
```text
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.001s

OK
```

- **Total de Testes:** 21 testes unitários.
- **Aprovações:** 21.
- **Falhas:** 0.
- **Erros:** 0.
- **Mensagens espúrias durante a importação:** Nenhuma.

---

## ⚠️ 5. Limitações Identificadas

1. **Inspeção Visual Humana da Interface Gráfica:**
   A automação comprovou que a classe `TetrisApp` instancia sem exceções, constrói os widgets, desenha no Canvas de $300 \times 540$ pixels e processa eventos. No entanto, a avaliação estética e fluidez da janela gráfica requer que o usuário a abra manualmente em sua área de trabalho (`python tetris_gui.py`).
2. **Suporte a Cores no Console:**
   A função `colored_board()` utiliza TrueColor ANSI (24 bits). O efeito visual dos blocos preenchidos requer um emulador de terminal compatível (como o Terminal do Windows, VS Code ou PowerShell moderno).

---

## 🏁 6. Conclusão

Todos os módulos do projeto (`exceptions.py`, `block.py`, `tetriminos.py`, `tetris.py`, `tetris_terminal.py`, `tetris_gui.py`) estão integrados, cumprem a arquitetura desacoplada do professor e passaram com **100% de aprovação** nos testes automatizados executáveis.

