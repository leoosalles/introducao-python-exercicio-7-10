# 🎮 Jogo da Velha

Implementação de um **Jogo da Velha (Tic-Tac-Toe) para dois jogadores** em Python puro, desenvolvida como solução do Exercício 7.10 de um curso de Introdução à Programação com Python.

---

## 📋 Descrição

O programa simula uma partida completa de Jogo da Velha no terminal, alternando turnos entre dois jogadores humanos. O tabuleiro é representado internamente como uma **lista de listas** (matriz 3×3), e as posições são mapeadas por meio de um dicionário de coordenadas que associa os números de 1 a 9 às respectivas células da grade.

---

## 🕹️ Como jogar

1. Execute o script no terminal:
   ```bash
   python jogo_da_velha.py
   ```
2. Ao iniciar, o programa exibe um mapa de referência com a numeração das posições:
   ```
    7 | 8 | 9
   ---+---+---
    4 | 5 | 6
   ---+---+---
    1 | 2 | 3
   ```
3. Os jogadores se alternam digitando o número da posição desejada.
4. **Jogador 1** marca com `X` e **Jogador 2** marca com `O`.
5. O jogo encerra quando um jogador vence ou todas as 9 posições forem preenchidas (empate).

---

## ✅ Funcionalidades

- Alternância automática de turnos entre Jogador 1 e Jogador 2
- Validação de entrada (aceita apenas dígitos de 1 a 9)
- Verificação de posição ocupada (impede sobreposição de marcações)
- Detecção de vitória nas 8 combinações possíveis:
  - 3 linhas horizontais
  - 3 colunas verticais
  - 2 diagonais
- Detecção de empate (todas as casas preenchidas sem vencedor)
- Exibição do tabuleiro atualizado a cada rodada

---

## 🗂️ Estrutura do código

| Elemento | Descrição |
|---|---|
| `tabuleiro` | Matriz 3×3 (`list[list[str]]`) que armazena o estado do jogo |
| `coordenadas_tabuleiro` | Dicionário que mapeia posições (1–9) para índices `(linha, coluna)` |
| `jogador` | String que controla de quem é o turno atual |
| `jogadas` | Contador de jogadas realizadas (limite: 9) |
| `venceu` | Flag booleana que encerra o loop ao detectar vitória |

---

## 🔧 Requisitos

- Python **3.6** ou superior
- Nenhuma biblioteca externa — apenas a biblioteca padrão do Python

---

## ▶️ Exemplo de execução

```
 X | O | X
---+---+---
 O | X |  
---+---+---
   | O | X

Jogador 1 - Digite o número da posição a ser marcada: 3

Jogador 1 venceu a partida!

 X | O | X
---+---+---
 O | X |  
---+---+---
   | O | X
```

---

## 📚 Contexto acadêmico

Este projeto foi desenvolvido como solução do **Exercício 7.10** do curso de Introdução à Programação com Python, cujo enunciado solicita:

> *"Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. Um jogo da velha pode ser visto como uma lista de três elementos, na qual cada elemento é outra lista, também com três elementos."*

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.
