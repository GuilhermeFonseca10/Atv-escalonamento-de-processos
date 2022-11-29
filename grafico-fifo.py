import matplotlib.pyplot as plt
import numpy as np

def fifo(numero):
    lista_de_processos = ["A","B","C","D"]
    processos = lista_de_processos[0:numero]

    tempo_do_processo = [np.random.randint(1,4) for i in range(numero)]
    processo_rodando = 0 
    controlador = 0 
    lista_de_tempo = []
    lista_espera = []

    for i in range(numero):
        lista_de_tempo.append(0)
        lista_espera.append(0)
    plt.style.use('ggplot')
    plt.ion()
    while processo_rodando < numero:
        if controlador < tempo_do_processo[processo_rodando]:
            lista_de_tempo[processo_rodando] = lista_de_tempo[processo_rodando]+1

            for i in range(processo_rodando +1, len(lista_espera)):
                lista_espera[i] = lista_espera[i]+1
            controlador = controlador + 1
        else:
            controlador = 0
            processo_rodando = processo_rodando+1
        x = processos
        y = lista_espera
        z = lista_de_tempo

        plt.barh(x, y, color='r')
        plt.barh(x,z, left=y, color='b')
        plt.ylabel("Tempo do processo")
        plt.xlabel("Processos")
        plt.title("Processos e tempo de processamento")

        plt.pause(1)
    plt.ioff()
    plt.show
    
fifo(4)
    