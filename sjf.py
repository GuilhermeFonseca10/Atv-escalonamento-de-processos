import matplotlib.pyplot as plt 
import numpy as np

def sjf(numero):
    lista_processo = ["A","B","C","D"]
    processo = lista_processo[0:numero]

 
    tempo_processo = [np.random.randint(1,4) for i in range(numero)]

    lista = []
    for i in range(numero):
        dict = {"name process":processo[i],"time process": tempo_processo[i]}
        lista.append(dict)

 
    lista = sorted(lista, key=lambda k : k['time process'])

    processo = []
    tempo_processo = []
    for i in lista:
        processo.append(i["name process"])
        tempo_processo.append(i["time process"])

    processo_rodando = 0 #index de controle de processo que roda atualmente
    controlador = 0 # controlador de tempo de processos
    lista_tempo = [] # lista auxiliar de tempo de processos 
    lista_espera = [] # lista auxiliar de tempo de espera

    for i in range(numero):
        #zerando as listas auxiliares
        lista_tempo.append(0)
        lista_espera.append(0)

    plt.style.use('ggplot')
    plt.ion()

    while processo_rodando < numero:
        if controlador < tempo_processo[processo_rodando]:
            lista_tempo[processo_rodando] = lista_tempo[processo_rodando]+1

            for i in range(processo_rodando +1, len(lista_espera)):
                lista_espera[i] = lista_espera[i]+1
            controlador = controlador + 1
        else:
            controlador = 0
            processo_rodando = processo_rodando+1
        x = processo
        y = lista_espera
        z = lista_tempo

        plt.barh(x, y, color='r')
        plt.barh(x,z, left=y, color='b')
        plt.ylabel("Processos")
        plt.xlabel("Tempo de processos")
        plt.title("Processos SJF")

        plt.pause(1)
    plt.ioff()
    plt.show
    
sjf(4)