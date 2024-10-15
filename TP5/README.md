# Relatório do TP5
## Autor: Marta Capa
## Data: 2024-10-9

### Resumo
O TP5 consistiu na criação de uma aplicação para gerir as salas de cinema de uma centro comercial. 
Cada sala pode estar ou não a exibir filmes, assim se o elemento de índice 2 de uma sala for "_" significa que aquela sala não está a exibir nehum filme naquele momento. 
As funcionalidades desta aplicação incluem, uma função que lista no monitor todos os filmes que estão em exibição nas salas do cinema, fazendo print do elemento de índice 2 de cada sala, se esse elemento não for "_". A funcionalidade 2 verifica se um lugar para um filme já está ocupado ou não, devolvendo True se não estiver e False no caso, averiguando primerio se esse luagr é maior do que a lotação da sala, ou seja, se o lugar existe. A terceira funcionalidade serve para vender bilhetes, que utiliza a segunda função para primeiro verificar se o lugar está disponível e de seguida cria um novo cinema adicionando o lugar à lista de lugares ocupados. A função 4 lista para cada sala o filme que está a ser exibido e o número de lugares disponíveis na sala. A quinta funcionalidade adiciona uma sala ao cinema, verificando primeiro se essa sala já existe.
Para além das funcionalidades pedidas criei também uma função que permite alterar o filme que está a ser exibido numa sala. Quando é utilizada e o filme é alterado, os lugares ocupados nessa sala passam a ser 0.