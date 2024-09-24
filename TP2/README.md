# Relatório do TP2
## Autor: Marta Capa
## Data: 2024-09-18

### Resumo 
O tpc2 consistiu na criação de um programa em phyton para jogar o jogo "Adivinha o número" com 2 modalidades, onde na modalidade 1 o computador pensa num número entre 0 e 100 e o utilizador tenta adivinhar e na modalidade 2 utilizador pensa num número entre 0 e 100 e o computador tenta adivinhar. Quem tenta adivinhar responde com "Acertou", "O número que pensei é Maior" ou "O número que pensei é Menor". Assim que o número for descoberto o programa termina e imprime o número de tentativas de que quem adivinhou precisou para chegar ao resultado.

Primeiro criei uma função para o utilizador escolher entre as duas modalidades, que no final chama a função da modalidade 1 ou da modalidade 2.
De seguida criei a função para a modalidade 1, onde usei a função randint para fazer o computadr gerar um número inteiro aleatório, no intervalo entre 0 e 100. Utilizando a estrutura ciclica while o computador lê os palpites do utilizador e responde com "O número que pensei é Maior" ou "O número que pensei é Menor" até o utilizador descobrir o número. Cada vez que o ciclo se repete é adicionado 1 ao número de tentativas do utilizador.
Por último, elaborei a função da modalidade 2 em que, de novo, com a função randidnt o computador gera um número inteiro, entre 0 e 100, e o utilizador responde com "O número que pensei é Maior" ou "O número que pensei é Menor". Se o palpite do computador for maior, através da função randint vai ser gerado um novo número aleatório, mas desta vez o intervalo é entre o palpite anterior mais 1 e 100. Se o número for menor, acontece o mesmo, porém o novo palpite estará entre 0 e o palpite anterio menos 1.

### Considerações
A mior deificuldade que tive na realização deste tpc foi fazer o programa gerar um número aleatório, uma vez que não foi falado nas aulas.