# Projeto: Busca de Caminho em Labirinto com Algoritmo A\*

## Descrição do Projeto

Este projeto implementa o algoritmo **A\*** (A Star) para encontrar o **menor caminho entre dois pontos em um labirinto** representado por uma matriz. O labirinto contém paredes (representadas por `1`), caminhos livres (`0`), um ponto de partida `S` e um ponto de chegada `E`.

## Introdução ao Problema

Encontrar o menor caminho em um labirinto é um problema clássico da ciência da computação. A ideia é guiar um "robô" ou agente do ponto inicial ao final, evitando obstáculos (paredes) e minimizando o número de passos. O algoritmo A\* é ideal para esse tipo de tarefa por combinar busca informada com heurística.

## Instruções para Configuração e Execução

### Requisitos

* Python 3.x instalado

### Execução

1. Clone ou baixe o repositório.
2. Execute o script com:

   ```bash
   python main.py
   ```

## Funcionamento do Algoritmo A\*

O A\* é um algoritmo de busca informada que encontra o menor caminho de forma eficiente ao utilizar dois fatores:

* **g(n):** o custo do caminho já percorrido até o nó `n`.
* **h(n):** a estimativa do custo restante até o objetivo (heurística).

A combinação desses dois valores resulta em:

$$
  f(n) = g(n) + h(n)
$$

Neste projeto:

* Utilizamos a **distância de Manhattan** como heurística, ideal para movimento em linhas e colunas.
* Apenas movimentos ortogonais (cima, baixo, esquerda, direita) são permitidos.
* O algoritmo utiliza uma **fila de prioridade (heap)** para escolher o próximo nó a ser explorado com base no menor `f(n)`.

## Explicação do Código

### 1. Heurística (função `heuristic`)

Calcula a distância de Manhattan entre dois pontos da matriz.

### 2. Função `a_star_search`

* Recebe a matriz, o ponto de partida e o ponto final.
* Utiliza uma fila de prioridade para decidir o próximo nó a ser explorado.
* Atualiza os custos com base nos movimentos e reconstrói o caminho final se a meta for alcançada.

### 3. Função `print_maze_with_path`

Imprime visualmente o labirinto com o caminho encontrado:

* `S` = início
* `E` = fim
* `*` = parte do caminho
* `0` = caminho livre
* `1` = parede

### 4. Execução

Define um labirinto com `S`, `E`, `0` e `1`. Converte `S` e `E` para `0` internamente e executa a busca.

## Exemplo de Entrada

```python
maze = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1]
]
```

## Saída Esperada

```
Caminho encontrado: [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com caminho destacado:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

## Referências

* [A\* Search Algorithm – Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
* [GeeksForGeeks – A\* Search](https://www.geeksforgeeks.org/a-search-algorithm/)
