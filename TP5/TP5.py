def menu():
    print(""" 
    (1) Listar filmes
    (2) Disponibilidade do lugar
    (3) Venda de bilhetes
    (4) Lugares disponíveis por filme
    (5) Inserir sala
    (6) Mudar Filme que está a ser exibido numa sala 
    (7) Encerrar aplicação
    """)


def listar(cinema):
    for sala in cinema:
        if sala[2] != "_":
            print (sala[2])
  
    
def disponivel(cinema, filme, lugar):
    res = False
    for sala in cinema:
        if filme == sala[2]:
            if lugar in sala[1]:
                res = False
            elif lugar > sala[0]:
                res = "Esse lugar não existe"
            else:
                res = True
    return res


def vendeBilhete(cinema, filme, lugar):
    if disponivel(cinema, filme, lugar) == True:
        for sala in cinema:
            if filme == sala[2]:
                sala[1].append(lugar)
                print(cinema)   
    elif disponivel(cinema, filme, lugar) == False:
        print("Esse lugar já está ocupado, escolha outro ou verifique se ainda há bilhetes disponíveis")
    else:
        print("Esse lugar não existe")
 
 
def listardisponibilidades(cinema):
    for sala in cinema:
        if sala[2] != "_":
            print(f"Está a ser exibido o filme {sala[2]}, o total de lugares disponíveis é {sala[0] - len(sala[1])}")


def inserirSala(cinema, sala):
    if sala in cinema:
        print("Esta sala já existe.")
    else:
        cinema.append(sala)
        

def mudarFilme(cinema, i, filme):
    sala = cinema[i]
    sala[1] = []
    sala[2] = filme
            

cinema1 = []


cond = True
while cond:
    menu()
    opcao = int(input("Indique qual operação quer realizar: "))

    if opcao == 1:
        listar(cinema1)
    elif opcao == 2:
        filme1 = input("Indique o filme que quer ver: ")
        lugar1 = int(input("Introduza o lugar que quer verificar: "))
        print(disponivel(cinema1, filme1, lugar1))
    elif opcao == 3:
        filme2 = input("Indique o filme que quer ver: ")
        lugar2 = int(input("Introduza o lugar que quer comprar: "))
        vendeBilhete(cinema1, filme2, lugar2)
    elif opcao == 4:
        listardisponibilidades(cinema1)
    elif opcao == 5:
        lotacao = int(input("Introduza a capacidade da sala: "))
        filmeNovo = input("Introduza o nome do filme que vai ser exibido na sala: ")
        salaNova = [lotacao, [], filmeNovo]
        inserirSala(cinema1, salaNova)
    elif opcao == 6:
        for i in range(len(cinema1)):
            print(i, cinema1[i])
        indice = int(input("Introduza o indice da sala que quer alterar: "))
        novoFilme = input("Intoduza o novo filme: ")
        mudarFilme(cinema1, indice, novoFilme)
    elif opcao == 7:
        cond == False