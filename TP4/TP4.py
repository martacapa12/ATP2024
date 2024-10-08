def menu():
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

variavel = []

import random 
def criaLista(tamanho):

    for i in range(tamanho):
        x = random.randint(0, 100)
        variavel.append(x)

def leLista(N):

    for num in range(N):
        x = int(input("Introduza o número: "))
        variavel.append(x)          

def somaLista(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return soma

def mediaLista(lista):
    if len(lista) == 0:
        res = 0
    soma = somaLista(lista)
    res = soma / len(lista)
    return res

def maiorLista(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

def menorLista(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor


def estaOrdenadaC(lista):
    res = "Sim"
    for i in range(0, len(lista) - 1):
        if lista[i] <= lista[i + 1] and res == "Sim":
            res = "Sim"
        else: 
            res = "Não"
    return res


def estaOrdenadaD(lista):
    res = "Sim"
    for i in range(0, len(lista) - 1):
        if lista[i] >= lista[i + 1] and res == "Sim":
            res = "Sim" 
        else: 
            res = "Não"
    return res

def unicos(lista, elem):
    if elem in lista:
        res = lista.index(elem)
    else:
        res = -1
    return res

cond = True
while cond == True:    
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        variavel = []
        tamanho = int(input("Intoduza o tamnho da lista: "))
        criaLista(tamanho)
    elif opcao == 2:
        variavel = []
        tamanho = int(input("Intoduza o tamnho da lista: "))
        leLista(tamanho)
    elif opcao == 3:
        res = somaLista(variavel)
        print(res)
    elif opcao == 4:
        res = mediaLista(variavel)
        print(res)
    elif opcao == 5:
        res = maiorLista(variavel)
        print(res)
    elif opcao == 6:
        res = menorLista(variavel)
        print(res)
    elif opcao == 7:
        res = estaOrdenadaC(variavel)
        print(res)
    elif opcao == 8:
        res = estaOrdenadaD(variavel)
        print(res)
    elif opcao == 9:
        elemento = int(input("Introduza o elelmento que quer procurar na lista: "))
        res = unicos(variavel, elemento) 
        print(res)
    elif opcao == 0:
        print(variavel)
        cond = False