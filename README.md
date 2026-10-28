# 🕹️ Tetris em Python + Tkinter

Projeto acadêmico colaborativo de desenvolvimento do clássico jogo **Tetris**, construído em linguagem **Python** com interface gráfica nativa em **Tkinter**.

---

## 🎯 1. Objetivo do Projeto

Este projeto tem finalidade estritamente pedagógica e colaborativa. Desenvolvido por uma equipe de **quatro alunos iniciantes**, o objetivo central é aplicar conceitos fundamentais de programação estruturada/modular, manipulação de interface gráfica no Tkinter e fluxo de trabalho em equipe utilizando controle de versão com **Git e GitHub**.

O projeto foi dividido em quatro partes modulares e independentes, permitindo que cada estudante se aprofunde em um aspecto da mecânica do jogo, culminando na integração harmoniosa de todos os componentes em um jogo completo e jogável.

> **Importante:** Nesta etapa inicial, o projeto contém apenas a **organização estrutural**, a documentação e os arquivos com comentários e marcadores `TODO`. Nenhuma lógica de jogo funcional foi implementada ainda.

---

## 🛠️ 2. Tecnologias Utilizadas e Ambiente Híbrido

- **Linguagem:** [Python 3](https://www.python.org/) (Versão recomendada: **Python 3.10 ou superior**, mínimo Python 3.8)
- **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html) (biblioteca gráfica padrão do Python)
- **Controle de Versão:** [Git](https://git-scm.com/) e [GitHub](https://github.com/) (Repositório Privado compartilhado)
- **Editores de Código Suportados:**
  - **Antigravity IDE:** Utilizado pelo proprietário do projeto.
  - **Visual Studio Code (VS Code):** Utilizado pelos outros três integrantes da equipe.

---

## 💻 3. Compatibilidade entre Antigravity e VS Code

Como a equipe utilizará editores diferentes, estabelecemos **10 Regras de Ouro** para garantir 100% de compatibilidade e evitar problemas de integração:

1. **Arquivos Python Padrão:** Todos os arquivos de código são arquivos comuns `.py`, sem sintaxes especiais, metadados ou dependências exclusivas de um editor.
2. **Sem Dependência de Extensões Proprietárias:** Nenhum recurso do jogo dependerá de plugins ou extensões exclusivas do Antigravity ou do VS Code.
3. **Caminhos Puramente Relativos:** É terminantemente proibido utilizar caminhos absolutos no código (ex: `C:\Users\lucas\...` ou `/home/usuario/...`). Todos os arquivos, importações e eventuais recursos devem usar caminhos relativos ao diretório do projeto.
4. **Consistência de Nomes e Pastas:** A estrutura de diretórios e a nomenclatura dos arquivos é fixa e idêntica para todos os integrantes.
5. **Git e GitHub como Canal Único Oficial:** Toda sincronização de código entre os editores é feita obrigatoriamente via Git e GitHub. Não há transferência de arquivos por e-mail, pen drive ou mensagens avulsas.
6. **Abertura Direta da Mesma Pasta:** A pasta raiz do projeto (`tetris-python-tkinter`) pode ser aberta diretamente no Antigravity ou no VS Code sem qualquer necessidade de recriar a estrutura.
7. **Fluxo Padronizado de Trabalho:** Todos os 4 integrantes utilizam os mesmos comandos de terminal para clonar, criar branches, commitar e enviar Pull Requests.
8. **Versões Compatíveis do Python:** Todos os integrantes devem utilizar Python 3.8+ (preferencialmente Python 3.10+ ou superior) e verificar o suporte ao Tkinter antes de codificar.
9. **Privacidade e Segurança de Configurações:** Arquivos de workspace locais (`.vscode/`, `.antigravity/`, `.idea/`), variáveis de ambiente locais e eventuais tokens estão explicitamente ignorados no `.gitignore`.
10. **Escopo Preservado:** Nenhum código funcional do Tetris foi implementado nesta etapa; todos os arquivos contêm apenas estrutura e comentários de planejamento.

---

## 👥 4. Identificação da Equipe, Editores e Responsabilidades

Preencha os campos abaixo com os dados dos quatro integrantes da equipe:

| Papel | Arquivo Responsável | Editor Utilizado | Nome do Integrante | Matrícula / E-mail | Usuário GitHub |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proprietário** | `parte1_tabuleiro.py` | **Antigravity** | _[Preencher Nome]_ | _[Preencher Matrícula]_ | _@[usuario]_ |
| **Integrante 2** | `parte2_pecas.py` | **VS Code** | _[Preencher Nome]_ | _[Preencher Matrícula]_ | _@[usuario]_ |
| **Integrante 3** | `parte3_colisoes.py` | **VS Code** | _[Preencher Nome]_ | _[Preencher Matrícula]_ | _@[usuario]_ |
| **Integrante 4** | `parte4_jogo_completo.py` | **VS Code** | _[Preencher Nome]_ | _[Preencher Matrícula]_ | _@[usuario]_ |

### Detalhamento das Atribuições:

1. **Integrante 1 (Proprietário) — Tabuleiro e Interface Visual (`parte1_tabuleiro.py`)**
   - Criação da janela da aplicação Tkinter.
   - Configuração do `Canvas` e cálculo da área útil do jogo.
   - Definição do tamanho das células (pixels) e dimensões da grade (largura x altura).
   - Renderização visual da grade, do fundo e das células preenchidas.

2. **Integrante 2 — Peças e Movimentação (`parte2_pecas.py`)**
   - Definição das 7 peças tradicionais do Tetris (I, J, L, O, S, T, Z) e suas cores.
   - Representação matemática das formas e seus estados de rotação.
   - Controle das coordenadas e movimentação da peça ativa (esquerda, direita, queda).

3. **Integrante 3 — Colisões e Eliminação de Linhas (`parte3_colisoes.py`)**
   - *Módulo de maior complexidade lógica esperada.*
   - Validação de limites da tela (paredes esquerda, direita e fundo).
   - Detecção de colisão entre a peça em movimento e blocos já fixados.
   - Fixação da peça no tabuleiro quando atinge o repouso.
   - Identificação de linhas completas, remoção dessas linhas, descida dos blocos superiores e contagem de linhas limpas.

4. **Integrante 4 — Integração e Controle Geral (`parte4_jogo_completo.py`)**
   - Ponto de entrada (`main`) da aplicação.
   - Importação e articulação dos módulos dos Integrantes 1, 2 e 3.
   - Gerenciamento do ciclo temporal do jogo (`after` do Tkinter).
   - Captura e mapeamento dos eventos do teclado (setas, espaço, pause).
   - Controle de pontuação, nível, aceleração de velocidade e tela de Game Over.
   - *Nota ética:* O Integrante 4 coordena a integração e não deve fazer o trabalho dos demais colegas.

---

## 📁 5. Estrutura do Projeto

O repositório é limpo e não contém arquivos proprietários ou desnecessários de configuração:

```text
tetris-python-tkinter/
│
├── README.md                 # Apresentação do projeto, compatibilidade, tutoriais e roteiro
├── .gitignore                # Protege contra caches do Python, arquivos de SO, VS Code e Antigravity
│
├── parte1_tabuleiro.py       # Esqueleto do módulo de tabuleiro e interface visual
├── parte2_pecas.py           # Esqueleto do módulo de peças, formas e movimentação
├── parte3_colisoes.py        # Esqueleto do módulo de colisões e eliminação de linhas
├── parte4_jogo_completo.py   # Esqueleto do módulo integrador e controle geral do jogo
│
└── tests/
    └── README.md             # Guia e diretrizes para testes futuros
```

---

## 🔗 6. Informações do Repositório Oficial

- **Proprietário:** Seventx77
- **Nome do Repositório:** `tetris-python-tkinter`
- **URL do Repositório:** [https://github.com/Seventx77/tetris-python-tkinter](https://github.com/Seventx77/tetris-python-tkinter)
- **URL para Clonagem (HTTPS):** `https://github.com/Seventx77/tetris-python-tkinter.git`
- **Branch Principal Prevista:** `main`

---

## ⚙️ 7. Como Convidar os Colegas no GitHub (Configuração Inicial)

Por padrão, apenas o proprietário do repositório (`Seventx77`) possui permissão de escrita no repositório privado. Para que os outros 3 integrantes (usuários do VS Code) possam enviar suas branches diretamente:

1. O proprietário deve acessar o repositório no GitHub: [https://github.com/Seventx77/tetris-python-tkinter](https://github.com/Seventx77/tetris-python-tkinter).
2. Clicar na aba superior **Settings** (Configurações).
3. No menu lateral esquerdo, clicar em **Collaborators** (Colaboradores).
4. Clicar no botão verde **Add people** (Adicionar pessoas).
5. Digitar o nome de usuário no GitHub ou e-mail de cada um dos outros 3 colegas e confirmar.
6. **Atenção:** Cada colega convidado receberá um e-mail com o convite (ou um alerta na barra de notificações do GitHub) e **deve aceitar o convite** antes de conseguir enviar qualquer branch.

---

## 🖥️ 8. Configuração do Ambiente e Abertura nos Editores

### A. No Antigravity IDE (Proprietário)
1. **Abrir a pasta do projeto:**
   - Abra o Antigravity.
   - Clique em **File > Open Folder...** (ou no botão de abrir pasta).
   - Navegue até a pasta `tetris-python-tkinter` e selecione-a.
2. **Abrir o Terminal Integrado:**
   - Use o atalho `Ctrl + '` (ou acesse o menu superior `Terminal > New Terminal`).
3. **Verificar Python e Git:**
   - No terminal, execute os comandos de verificação detalhados na seção 9 (Passo 1).

---

### B. No Visual Studio Code (Integrantes 2, 3 e 4)
1. **Abrir a pasta do projeto:**
   - Abra o VS Code.
   - Clique em **File > Open Folder...** (ou use o atalho `Ctrl + K, Ctrl + O`).
   - Selecione a pasta clonada `tetris-python-tkinter`.
   - *Nota:* Não é necessário criar nenhum arquivo `.code-workspace` nem pastas adicionais. O VS Code reconhecerá os arquivos Python imediatamente.
2. **Extensão Opcional (Recomendada para conveniência):**
   - Na barra lateral esquerda do VS Code, clique no ícone de **Extensions** (`Ctrl + Shift + X`).
   - Procure por `Python` (desenvolvida pela Microsoft) e clique em **Install**. Essa extensão oferece apenas coloração de código e autocompletar; o código funcionará perfeitamente com ou sem ela.
3. **Abrir o Terminal Integrado:**
   - Use o atalho `Ctrl + '` (ou acesse o menu superior `Terminal > New Terminal`).
4. **Verificar Python e Git:**
   - No terminal do VS Code, execute os comandos de verificação detalhados na seção 9 (Passo 1).

---

## 🚀 9. Tutorial Passo a Passo de Git e GitHub para Iniciantes

Este tutorial é válido tanto para quem usa o terminal integrado do **Antigravity** quanto para quem usa o terminal integrado do **VS Code**.

### Passo 1: Verificar se Git, Python e Tkinter estão instalados
No terminal do seu editor (Antigravity ou VS Code), digite:

```bash
# 1. Verifica o Git
git --version

# 2. Verifica o Python (se python não responder no Windows, tente py --version)
python --version
```
Em seguida, faça o teste interativo do **Tkinter**:
```bash
python -m tkinter
```
> Uma pequena janela gráfica intitulada *"Tk"* com botões de exemplo deve aparecer na sua tela. Feche-a para confirmar que a interface gráfica está funcionando no seu sistema operacional!
> *(Em distribuições Linux baseadas em Debian/Ubuntu, caso o comando falhe, basta instalar com `sudo apt install python3-tk`).*

---

### Passo 2: Clonar o repositório oficial
Navegue até a pasta de sua preferência e clone o repositório:
```bash
git clone https://github.com/Seventx77/tetris-python-tkinter.git
cd tetris-python-tkinter
```

> **Atenção ao Primeiro Envio (Repositório Vazio ou Divergência):**
> Se o repositório remoto estiver vazio no GitHub e a estrutura inicial tiver sido gerada na máquina local do proprietário, verifique com `git status` e `git remote -v`. O proprietário deve inicializar o Git (`git init`), conectar a origem remota (`git remote add origin https://github.com/Seventx77/tetris-python-tkinter.git`), conferir que não está sobrescrevendo nada indesejado e enviar a branch `main` inicial. **Nunca use `git push --force` sem extrema certeza**, para não apagar o trabalho de ninguém.

---

### Passo 3: Abrir a pasta no seu editor
- **Se você for o Proprietário:** Abra a pasta no **Antigravity** conforme a Seção 8A.
- **Se você for um dos Integrantes:** Abra a pasta no **VS Code** conforme a Seção 8B.

---

### Passo 4: Verificar o estado do repositório
Antes de começar qualquer trabalho, confira em qual branch você está:
```bash
git status
```

---

### Passo 5: Criar sua branch própria de trabalho
**Regra de ouro:** Ninguém deve alterar diretamente a branch `main`! Cada integrante deve criar e trabalhar na sua branch específica:

```bash
# Integrante 1 (Proprietário - Antigravity):
git switch -c feature/parte1-tabuleiro

# Integrante 2 (Peças - VS Code):
git switch -c feature/parte2-pecas

# Integrante 3 (Colisões - VS Code):
git switch -c feature/parte3-colisoes

# Integrante 4 (Integração - VS Code):
git switch -c feature/parte4-integracao
```
*(O comando `git switch -c` cria a branch e muda para ela instantaneamente).*

---

### Passo 6: Editar seu arquivo e adicionar alterações
Após editar o arquivo sob sua responsabilidade, adicione as alterações para a área de preparação (*staging*):
```bash
# Exemplo para o Integrante 2:
git add parte2_pecas.py

# Ou para adicionar os arquivos modificados:
git add .
```

---

### Passo 7: Registrar alterações com commit
Crie um commit claro em português descrevendo sua evolução:
```bash
git commit -m "Define matrizes das 7 pecas e funcoes de rotacao"
```

---

### Passo 8: Publicar sua branch no GitHub
Na primeira vez que for enviar sua nova branch ao repositório:
```bash
# Exemplo para a branch do Integrante 2:
git push -u origin feature/parte2-pecas
```
*(Nos envios futuros na mesma branch, bastará digitar apenas `git push`).*

---

### Passo 9: Criar um Pull Request (PR) no GitHub
1. Abra o navegador em: [github.com/Seventx77/tetris-python-tkinter](https://github.com/Seventx77/tetris-python-tkinter).
2. O GitHub exibirá uma faixa amarela com o botão: **"Compare & pull request"**. Clique nele.
3. Certifique-se de que a base é `main` e a comparação é a sua branch (ex: `feature/parte2-pecas`).
4. Escreva um resumo amigável explicando o que você programou.
5. Clique em **"Create pull request"**.

---

### Passo 10: Revisar e integrar as alterações (Code Review)
1. Antes do merge, os colegas de equipe abrem a aba **"Files changed"** no GitHub e revisam o código.
2. Com a aprovação de todos, clica-se em **"Merge pull request"** e depois em **"Confirm merge"**.
3. O código daquela parte agora faz parte da `main` oficial!

---

### Passo 11: Atualizar a cópia local com git pull
Após qualquer merge na `main` no GitHub, todos os colegas devem atualizar suas máquinas locais para receber o trabalho integrado:
```bash
# 1. Muda para a main
git switch main

# 2. Puxa as alterações mais recentes
git pull origin main
```
Para trazer essas novidades para a sua branch individual de trabalho:
```bash
git switch feature/sua-branch
git merge main
```

---

### Passo 12: Como reconhecer e resolver conflitos com cuidado
Se dois integrantes editarem as mesmas linhas de código, o Git indicará um conflito durante o merge:
1. O Git colocará marcações no arquivo conflitante:
   ```text
   <<<<<<< HEAD
   (O código que estava na sua branch)
   =======
   (O código que veio da main ou do colega)
   >>>>>>> main
   ```
2. **Comunique-se:** Chame o colega no chat ou chamada e analisem juntos o trecho.
3. Edite o arquivo no seu editor (VS Code ou Antigravity), escolha o código correto e apague as linhas `<<<<<<<`, `=======` e `>>>>>>>`.
4. Finalize o processo:
   ```bash
   git add <arquivo_resolvido>
   git commit -m "Resolve conflito de integracao entre modulos"
   git push
   ```

---

## 🧩 10. Pendências de Planejamento para a Integração Futura

Os quatro arquivos **não funcionarão juntos automaticamente** apenas por existirem no mesmo diretório. Antes de qualquer pessoa começar a escrever código, a equipe deve se reunir e definir:

1. **Representação do Tabuleiro:**
   - Será uma matriz (lista de listas 20x10) de números (0 para vazio, 1 a 7 para peças) ou de strings com códigos hexadecimais de cores?
2. **Armazenamento e Formato das Peças:**
   - As peças serão matrizes (ex: 3x3 ou 4x4) rotacionadas matematicamente ou listas com as 4 coordenadas relativas `[(x1,y1), (x2,y2), ...]` pré-calculadas para cada uma das 4 rotações?
3. **Comunicação entre Módulos:**
   - Utilizaremos Programação Orientada a Objetos (classes `Tabuleiro`, `Peca`, `Jogo`) ou funções puras compartilhando um dicionário de estado?
4. **Responsabilidade do Desenho:**
   - O `parte1_tabuleiro.py` apenas oferecerá uma função genérica de pintar blocos, ou receberá o estado completo para renderizar de uma vez só?
5. **Verificação de Colisões:**
   - O módulo de colisão receberá a peça e a matriz do tabuleiro a cada tentativa de movimento e responderá com um booleano (`True`/`False`)?
6. **Coordenação do Laço Temporal:**
   - Como o `parte4_jogo_completo.py` sincronizará a taxa de queda das peças com os eventos de teclado sem travar a interface do Tkinter?

> **Ação recomendada:** Façam uma conversa de alinhamento para responder esses 6 pontos antes de iniciar a codificação!

---

## 🎓 11. Roteiro de Apresentação para o Professor

Quando o projeto estiver pronto, sugerimos este roteiro para a apresentação:

1. **Abertura e Apresentação da Equipe (1 a 2 min):**
   - Apresentação dos 4 integrantes, seus papéis e a divisão de ferramentas (Antigravity para o proprietário, VS Code para os demais integrantes).
   - Destaque para o uso de ferramentas padrão e universais sem atritos de compatibilidade.
2. **Demonstração do Fluxo Colaborativo no GitHub (2 a 3 min):**
   - Mostrar o repositório privado no GitHub.
   - Exibir as branches, Pull Requests revisados e histórico de commits de cada participante.
3. **Explicação Modular dos Componentes (3 a 4 min):**
   - *Integrante 1:* Explica o Canvas e a grade visual no Tkinter.
   - *Integrante 2:* Explica a matemática das 7 peças e o sistema de rotação.
   - *Integrante 3:* Explica os algoritmos de colisão, fixação e eliminação de linhas.
   - *Integrante 4:* Explica a orquestração do loop principal, eventos de teclado e controle de pontuação.
4. **Demonstração do Jogo em Ação (3 a 5 min):**
   - Executar `python parte4_jogo_completo.py`.
   - Jogar uma partida: demonstrar movimentação, rotação, eliminação de linhas, pontuação e Game Over.
5. **Conclusão e Lições Aprendidas (1 a 2 min):**
   - Compartilhar a experiência do trabalho em equipe com editores híbridos (Antigravity + VS Code), superação de conflitos no Git e modularização em Python.
