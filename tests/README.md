# Pasta de Testes (`tests/`)

Bem-vindos à pasta de testes do projeto **Tetris Python + Tkinter**!

## 📌 Objetivo desta Pasta
Esta pasta foi reservada para armazenar os **testes automatizados e manuais** do nosso jogo conforme o desenvolvimento avançar.

Os testes servem para:
1. **Verificar as regras do jogo:** Garantir que o Tetris se comporte exatamente como esperado pelas regras clássicas.
2. **Prevenir e encontrar bugs:** Identificar erros de lógica rapidamente antes da entrega final.
3. **Facilitar a integração:** Provar que os módulos criados pelos diferentes integrantes funcionam bem em conjunto sem quebrar partes uns dos outros.

---

## ⚠️ Status Atual
> **Nenhum teste foi implementado nesta etapa.**
>
> Como os módulos do jogo ainda estão em fase de planejamento e não possuem código funcional, os testes serão criados posteriormente, acompanhando a evolução de cada funcionalidade.

---

## 💡 Exemplos de Testes Planejados para o Futuro
Quando os módulos começarem a ser codificados, poderemos criar pequenos scripts de teste para verificar:
- **Testes de Peças (`parte2_pecas.py`):**
  - Todas as 7 peças têm os formatos e rotações corretos?
  - A peça gira corretamente em 360 graus e volta ao estado inicial?
- **Testes de Colisões (`parte3_colisoes.py`):**
  - A peça é impedida de atravessar as paredes laterais e o chão?
  - A colisão contra peças já paradas no tabuleiro funciona?
  - Uma linha cheia é removida corretamente e a contagem de pontos é calculada?
- **Testes de Integração (`parte4_jogo_completo.py`):**
  - O estado de Game Over é acionado quando as peças chegam ao topo?
  - O sistema de pontuação e aumento de velocidade responde às linhas eliminadas?

---
*Mantenha esta pasta organizada. Novos scripts de teste deverão ser adicionados aqui conforme combinado com a equipe.*
