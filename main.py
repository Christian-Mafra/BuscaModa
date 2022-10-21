#subprograma
from tarfile import LENGTH_NAME


def preenche(numero):
    lida = input()
    while lida != "":
        numero.append(lida)
        lida = input()
    return numero

def buscaModa(valores):
    auxiliar = [0]*len(valores)
    for indice in range(len(valores)):
        auxiliar[indice] = 1
        for varre in range(indice+1,len(valores)):
            if valores[varre] == valores[indice]:
                auxiliar[indice] += 1
    ondeModa = 0

    for ind in range(1, len(auxiliar)):
        if auxiliar[ind] > auxiliar[ondeModa]:
            ondeModa = ind
    return valores[ondeModa]


#principal
numero = list()
valores = preenche(numero)
moda = buscaModa(valores)
print(moda)