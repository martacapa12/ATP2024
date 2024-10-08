# Relatório do TP4
## Autor: Marta Capa
## Data: 2024-10-2

### Resumo
O TP4 consistiu na criação de uma aplicação em python que coloca no monitor um menu que oferece ao utilizador 10 opções. Para a elaborar criei uma função para o menu, em que no final o utilizador insere qual das operações quer executar, outras nove para as primeiras 9 opções, um ciclo while que se repete enquanto cond = True, executando repetidamente a função menu e de seguida a opção que o utilizador indicou.
Na opção 1 o utilizador insere um número inteiro, e o computador criar uma lista com esse tamnho,de números aleatórios entre 1 e 100. Na segunda opção, acontece o mesmo mas dsta vez é o utilizador que insere quais os números da lista. 
Nas operações seguites vai ser utilizada a variável criada nas opções anteriores (será usada a última lista que o utilizaodr tenha escolhido criar).
A opção 3 devolve a soma dos componentes da variável no momento, a 4 a média, a 5 o maior componente e a 6 o menor. Para a operação 7, cada elemento da lista, exceto o último, será comparado com aquele que vem depois, e se o de menor índice for sempre menor, ou seja, a lista é considerada crescente, a aplicação devolve Sim, na hipótese de não se verificar a condição em algum caso a aplicação devolve imediatamente Não. Na operação 8 acontece o oposto e é averiguado se a lista está ordenada de modo decrescente. A opção 9, procura um elemento, inserido pelo utilizador na lista, caso o encontre, através da função index, devolve o índice do elemento e na situação contrária devolve -1.
Por fim, na ultima opção, cujo número correspondente é 0, a aplicação imprime a lista que está guardade naquele momento e passa a considerar cond = False,logo a aplicação termina.