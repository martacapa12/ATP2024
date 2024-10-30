def menu():
    print("""
          (1) Criar tabela metereológica
          (2) Temperatura média de cada dia 
          (3) Guardar uma tabela num ficheiro
          (4) Carregar uma tabela metereológica de um ficheiro
          (5) Temperatura mais baixa registada na tabela
          (6) Amplitude térmica em cada dia
          (7) Dia com maior precipitação na tabela
          (8) Dias em que a precipitação foi maior do que um valor
          (9) Maior número de dias em que a precipitação foi menor do que um valor
          (10) Criar um gráfico com os valores de temperatura mínima, máxima e precipitação
          (0) Fechar a aplicação
          """)


def criarTab(n):
    for i in range(n):
        ano = int(input("Introduza o ano: "))
        mes = int(input("Introduza o mês: "))
        dia = int(input("Introduza o dia: "))
        temp_min = float(input("Introduza a temperatura mínima: "))
        temp_max = float(input("Introduza a temperatura máxima: "))
        prec = float(input("Introduza o valor da precipitação: "))
        tabelaMeteo.append(((ano, mes, dia), temp_min, temp_max, prec))

def medias(t):
    res = []
    for dia in t:
        media = (dia[1] + dia[2]) / 2
        res.append((dia[0], media))
    return res


def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, min, max, prec in t:
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia}&{min}&{max}&{prec}\n"
        file.write(registo)           
    file.close()
    
    
def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for linha in file:
        linha = linha[:-1]        
        campos = linha.split("&")          
        data, min, max, prec = campos
        ano, dia, mes = data.split("-")
        
        res.append(((int(ano), int(dia), int(mes)), float(min), float(max), float(prec)))
    file.close()
    return res


def minMin(t):
    minima = t [0][1]
    for dia in t:
        minimaDia = dia[1]
        if minimaDia < minima:
            minima = minimaDia
    return minima


def amplTerm(t):
    res = []
    for data, min, max, prec in t:
        amplitude = max - min
        res.append((data, amplitude))
    return res 


def maxChuva(t):
    res = []
    max_prec = t [0][3]
    max_data = t [0][0]
    for dia in t:
        precDia = dia[3]
        if precDia > max_prec:
            max_prec = precDia
            max_data = dia[0]
    return (max_data, max_prec)


def diasChuvosos(t, p):
    res = []
    for dia in t:
        if dia[3] > p:
            res.append((dia[0], dia[3]))
    return res


def menDiasPrec(t, p):
    consec_local = 0
    consec_max = 0
    for data, min, max, prec in t:
        if prec < p:
            consec_local = consec_local + 1
        else:
            if consec_local > consec_max:
                concec_max = consec_local
            consec_local = 0
            
    if consec_local > consec_max:
        concec_max = consec_local
    return consec_max


import matplotlib.pyplot as plt

def grafTabMeteo(t):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    tempMin = [min for _, min, *_ in t]
    tempMax = [max for _, _, max, *_ in t]
    prec = [prec for _, _, _, prec in t]

    plt.plot(datas, tempMin)
    plt.title("Temperatura Minima")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.show()
    
    plt.plot(datas, tempMax)
    plt.title("Temperatura Máxima")
    plt.xlabel("Data")
    plt.ylabel("Temperatura ºC")
    plt.show()
    
    plt.bar(datas,prec)
    plt.title("Precipitação")
    plt.xlabel("Data")
    plt.ylabel("Precipitação mm")
    plt.show()

tabelaMeteo = []

cond = True 

while cond:
    menu()
    opcao = int(input("Introduza a opreração que quer realizar: "))
    if opcao == 1:
        num = int(input("Introduza o tamanho da tabela: "))
        criarTab(num)
    elif opcao == 2:
        print(medias(tabelaMeteo))
    elif opcao == 3:
        ficheiro = input("Introduza o nome do ficheiro: ")
        guardaTabMeteo(tabelaMeteo, ficheiro)
    elif opcao == 4:
        ficheiro = input("Introduza o nome do ficheiro: ")
        print(carregaTabMeteo(ficheiro))
    elif opcao == 5:
        print(minMin(tabelaMeteo))
    elif opcao == 6:
        print(amplTerm(tabelaMeteo))
    elif opcao == 7:
        print(maxChuva(tabelaMeteo))
    elif opcao == 8:
        precipitacao = int(input("Introduza o valor limite de precipitação: "))
        print(diasChuvosos(tabelaMeteo, precipitacao))
    elif opcao == 9:
        precipitacao = int(input("Introduza o valor limite de precipitação: "))
        print(menDiasPrec(tabelaMeteo, precipitacao))
    elif opcao == 10:
        print(grafTabMeteo(tabelaMeteo))
    elif opcao == 0:
        cond = False
    else:
        print("Essa opção não existe, escolha uma operação válida.")