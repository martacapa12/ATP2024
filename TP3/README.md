# Relatório do TP3
## Autor: Marta Capa
## Data: 2024-09-25

### Resumo 
O tp3 consistiu na criação de um programa em python para o Jogo dos 21 Fósforos. No ínicio do jogo há 21 e cada jogador pode tirar 1, 2, 3 ou 4 fósforos na sua vez de jogar, quem tiara o ultimo fósforo perde. O jogo possui dois modos, no modo 1 o utilizador começa a jogar e no modo dois começa o computador.
No modo 1 o utilizador começa jogar. A estratégia que o segundo jogador tem de seguir para vencer é o número de fósforos que tira ser igual a 5 menos o número de fósforos retirados pelo primrreio jogador. Assim em cada ronda são retirados sempre 5 fósforos, e no início da quinta ronda vai restar apenas 1 fósforo fazendo com que o primeiro jogador perca. Portanto, neste modo o computador ganha sempre.
No modo 2 o computador começa a jogar. Neste caso o utilizador apenas perde se cometer algum erro de cálculo, ou seja, se restarem 5, 4, 3 ou 2 fósforos quando for a vez do computador jogar.