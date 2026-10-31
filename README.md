# 🕹️ Tetris em Python + Tkinter

Projeto acadêmico colaborativo de desenvolvimento do clássico jogo **Tetris**, estruturado rigorosamente segundo a **arquitetura orientada a objetos proposta pelo professor**, implementado em **Python** com interfaces para **Console (Terminal)** e **Interface Gráfica (Tkinter)**.

---

## 🎯 1. Objetivo do Projeto

Este projeto tem finalidade estritamente pedagógica e acadêmica. Desenvolvido por uma equipe de **quatro alunos iniciantes**, o objetivo principal é aplicar conceitos fundamentais de programação orientada a objetos (POO), tais como:

- **Classes, Objetos e Imutabilidade** (criação de blocos imutáveis em `block.py`).
- **Herança e Polimorfismo** (classe abstrata `Tetrimino` e as 7 peças clássicas em `tetriminos.py`).
- **Tratamento de Exceções Personalizadas** (`GamerError`, `InvalidBlockError`, `InvalidRotationError` em `exceptions.py`).
- **Separação entre Modelo e Visão** (o motor de regras `tetris.py` não depende de nenhuma interface visual).
- **Múltiplas Interfaces Desacopladas** (interface textual em console `tetris_terminal.py` e interface gráfica em Tkinter `tetris_gui.py`).
- **Trabalho Colaborativo via Git e GitHub** (uso de branches individuais, revisões de código e Pull Requests).

> ⚠️ **IMPORTANTE: A PROGRAMAÇÃO AINDA NÃO COMEÇOU**  
> Nesta etapa preparatória, **nenhum código funcional foi implementado**. Todos os módulos contêm **exclusivamente comentários explicativos e marcadores `# TODO`**. O projeto está estruturado e documentado para que cada integrante inicie sua parte de forma independente e coordenada.

---

## 🏛️ 2. Arquitetura do Professor e Divisão em Camadas

A arquitetura do projeto foi desenhada para desacoplar a lógica das regras do jogo da forma como ele é exibido ao usuário:

```text
┌─────────────────────────────────────────────────────────────────┐
│                     CAMADA DE APRESENTAÇÃO                      │
│   tetris_terminal.py (Texto)        tetris_gui.py (Tkinter)     │
└────────────────────────────────┬────────────────────────────────┘
                                 │ consome (apenas consulta e comandos)
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
│             exceptions.py (Hierarquia de erros GamerError)      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 3. Estrutura de Arquivos do Projeto

A organização de diretórios e arquivos foi padronizada da seguinte forma:

```text
tetris-python-tkinter/
│
├── README.md                 # Documentação completa, tutoriais de ambiente e fluxo Git
├── .gitignore                # Proteção contra caches, ambientes virtuais e arquivos locais
│
├── exceptions.py             # Hierarquia oficial de exceções (GamerError, InvalidBlockError, InvalidRotationError)
├── block.py                  # Bloco imutável constituinte com coordenadas (x, y)
├── tetriminos.py             # Classe abstrata Tetrimino e as 7 peças (I, J, L, O, S, T, Z)
├── tetris.py                 # Modelo central: grade 10x18, física, colisões e controle
├── tetris_terminal.py        # Interface textual em console para testes rápidos
├── tetris_gui.py             # Interface gráfica construída com Tkinter (Canvas, timer 500ms)
│
└── tests/
    └── README.md             # Guia de testes unitários e de integração futuros
```

---

## 👥 4. Divisão dos Integrantes e Responsabilidades Definidas

A divisão de tarefas entre os quatro integrantes **já está formalmente definida e fixada**. Cada integrante é responsável exclusivo pelo desenvolvimento do seu módulo:

| Integrante | Arquivos Atribuídos | Responsabilidade Definida | Editor de Trabalho |
| :--- | :--- | :--- | :--- |
| **Integrante 1 (Proprietário)** | `exceptions.py`<br>`block.py` | Exceções oficiais (`GamerError`) e classe `Block` imutável com validação de negativos. | **Antigravity** |
| **Integrante 2** | `tetriminos.py` | Classe abstrata `Tetrimino`, cálculo de `box_size`, fórmula de rotação e as 7 subclasses. | **VS Code** |
| **Integrante 3** | `tetris.py` | Modelo de jogo: matriz 10x18, posicionamento inicial, colisão, travamento (`_lock`) e linhas. | **VS Code** |
| **Integrante 4** | `tetris_terminal.py`<br>`tetris_gui.py` | Interfaces com usuário: console ANSI e aplicação Tkinter com Canvas, timer de 500ms e botão Reiniciar. | **VS Code** |

> **Nota de colaboração:** O Integrante 4 coordena as interfaces que consomem `Tetris`, sem implementar as regras dos outros módulos. Cada integrante testa sua parte antes de integrá-la.

---

## 🪜 5. Ordem de Implementação Recomendada pelo Professor

Para garantir uma integração suave, o desenvolvimento deve seguir o encadeamento de dependências:

1. **Fase 1 — Base (`exceptions.py` e `block.py`):**
   - Implementação das exceções e da classe `Block`.
   - É a base para as formas das peças.
2. **Fase 2 — Formas e Rotações (`tetriminos.py`):**
   - Implementação da classe base `Tetrimino` e das 7 subclasses clássicas.
   - Teste no console com `print(peca)` e `peca.right_rotate()`.
3. **Fase 3 — Motor de Regras (`tetris.py`):**
   - Implementação do tabuleiro 10x18 (`_grid`), posicionamento, colisões, `_lock()` e `_clear_rows()`.
4. **Fase 4 — Interfaces (`tetris_terminal.py` e `tetris_gui.py`):**
   - Interface textual primeiro (para validar jogabilidade no terminal).
   - Interface gráfica Tkinter em seguida (Canvas com timer de queda de 500ms).

---

## 🎮 6. Regras e Especificações Oficiais do Tetris (PDF)

- **Dimensões do Tabuleiro:** 10 colunas de largura por 18 linhas de altura (`DEFAULT_WIDTH = 10`, `DEFAULT_HEIGHT = 18`).
- **Sistema de Coordenadas:** Padrão Canvas ($x$ coluna cresce para a direita; $y$ linha cresce para baixo).
- **Indexação da Matriz Interna:** `_grid[coluna][linha]`. Posições vazias contêm `None`; posições fixadas contêm a cor hex (`#rrggbb`).
- **Peça Ativa:** Não é gravada no `_grid` enquanto está em queda, somente quando for fixada (`_lock()`).
- **Fórmula de Rotação Horária (90°):**
  $$\text{nova\_x} = \text{box\_size} - 1 - y, \quad \text{nova\_y} = x$$
- **Cálculo do `box_size`:** $1 + \max(x, y)$ entre todos os blocos da forma original (rotação 0).
- **Posicionamento da Nova Peça:** Centralizada no topo: `col = (width - box_size) // 2`, `row = 0`.
- **Regra de Fim de Jogo:**
  - Ocorre se a nova peça sorteada não couber imediatamente na posição de entrada.
  - **Depois do fim de jogo, os comandos de movimento não têm efeito.**
- **Desacoplamento das Interfaces:**
  - As interfaces **não implementam nenhuma regra de física ou colisão**. Elas apenas consultam `width`, `height`, `color_at(col, row)`, `game_over` e enviam os comandos de ação.

---

## 💻 7. Compatibilidade entre Antigravity e VS Code

- **Arquivos Python Padrão:** O código usa Python padrão sem recursos proprietários.
- **Caminhos Relativos:** Todas as importações usam referências diretas no mesmo pacote.
- **Ambiente Limpo:** Arquivos de workspace locais (`.vscode/`, `.antigravity/`, caches) estão devidamente ignorados no `.gitignore`.

---

## 🚀 8. Fluxo Oficial Git e GitHub: Branches e Pull Requests

### Regra Fundamental
**Ninguém desenvolve diretamente na branch `main`!** A branch `main` é reservada exclusivamente para código revisado e aprovado. Cada integrante deve trabalhar obrigatoriamente em sua própria branch.

---

### Passo 1: Abrir o terminal no editor e verificar ambiente
```bash
git --version
python --version
python -m tkinter
```

---

### Passo 2: Atualizar a cópia local da `main`
Antes de criar ou atualizar sua branch:
```bash
git switch main
git pull origin main
```

---

### Passo 3: Criar e ativar sua branch individual de trabalho
Cada integrante cria sua respectiva branch a partir da base atualizada:

```bash
# Integrante 1 (Exceções e Bloco):
git switch -c feature/bloco-excecoes

# Integrante 2 (Tetraminós e Rotação):
git switch -c feature/tetriminos

# Integrante 3 (Motor Tetris):
git switch -c feature/motor-tetris

# Integrante 4 (Interfaces Terminal e GUI):
git switch -c feature/interfaces
```

---

### Passo 4: Fazer alterações e registrar commits claros
Após editar seu arquivo atribuído:
```bash
git status
git add <arquivo_modificado>
git commit -m "Implementa validacao de coordenadas em Block"
```

---

### Passo 5: Publicar a branch individual no GitHub
Na primeira publicação da sua branch:
```bash
git push -u origin feature/sua-branch
```
*(Nos envios seguintes na mesma branch, basta executar `git push`).*

---

### Passo 6: Abrir um Pull Request (PR) no GitHub
1. Acesse o repositório oficial: [https://github.com/Seventx77/tetris-python-tkinter](https://github.com/Seventx77/tetris-python-tkinter).
2. O GitHub exibirá o botão verde **"Compare & pull request"**. Clique nele.
3. Verifique se a **base branch** é `main` e a **compare branch** é a sua (`feature/sua-branch`).
4. Dê um título claro e descreva em tópicos o que foi implementado e como testar.
5. Clique em **"Create pull request"**.

---

### Passo 7: Revisão de Código e Integração (Merge)
1. Pelo menos um colega de equipe deve revisar as alterações na aba **"Files changed"** do Pull Request.
2. Com a aprovação da equipe, o PR é integrado clicando em **"Merge pull request"** e depois **"Confirm merge"**.
3. Em seguida, todos os integrantes executam em suas máquinas locais:
   ```bash
   git switch main
   git pull origin main
   ```
   E atualizam suas branches individuais com `git merge main` para manter todos os trabalhos sincronizados.

---

## 🧪 9. Planejamento de Testes Futuros

Consulte o documento [tests/README.md](file:///c:/Users/lucas/Documents/tetris-python-tkinter/tests/README.md) para verificar os testes planejados para cada classe e método do jogo antes de iniciar a programação.

---

## 🎓 10. Roteiro para Apresentação ao Professor

1. **Abertura e Arquitetura (2 min):** Apresentar a equipe e a arquitetura em 4 camadas (Domínio, Formas, Motor e Interfaces).
2. **Fluxo Colaborativo no GitHub (2 min):** Mostrar o histórico de branches, revisões de código e Pull Requests aprovados.
3. **Módulos Individuais (4 min):** Cada integrante explica seu arquivo, destacando herança, imutabilidade, encapsulamento e regras.
4. **Demonstração Prática (4 min):**
   - Execução de `python tetris_terminal.py` comprovando a lógica no console.
   - Execução de `python tetris_gui.py` jogando na interface gráfica Tkinter.
5. **Conclusão (1 min):** Lições aprendidas em POO e trabalho colaborativo.
