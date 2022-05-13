import random
import math
from scipy.stats import norm


def funcion_grado5(x1, x2, x3, x4, x5):
    return x1 * (x2**2) * (x3**3) * (x4**4) * (x5**5)

def volumen_funcion(n,semilla,limites):
    s = 0
    t = 0
    random.seed(semilla)
    #print(limites)
    for j in range(1,n+1):
        x1 = random.uniform(0,1)   
        x2 = random.uniform(0,1)
        x3 = random.uniform(0,1)
        x4 = random.uniform(0,1)
        x5 = random.uniform(limites[0],limites[1])
        #print(x1)
        z = funcion_grado5(x1,x2,x3,x4,x5)
        if j>1:
            t += (1-1/j)*((z-s/(j-1))**2) 
        s += z
    estimador = (s/n)
    var_funcion = t/(n-1)
    var_estimador = var_funcion/n
    return estimador, var_funcion, var_estimador

def intervalo(n, delta, estimador, var_estimador):
    term1 = norm.ppf(1-delta/2)
    term2 = math.sqrt(var_estimador/n)
    return [estimador-term1*term2,estimador+term1*term2]

def valor_n(delta, epsilon, varianza):
    term1 = norm.ppf(1-delta/2)**2
    return math.ceil((term1*varianza) / (epsilon**2))

def valor_epsilon(delta, n, varianza):
    return math.sqrt(((norm.ppf(1-delta/2)**2)*varianza)/(n))

def in_rango(valor_exacto, rango):
    return valor_exacto>=rango[0] and valor_exacto<=rango[1]

if __name__ == "__main__":

    # Lo limites de cada region (del lado derecho) es numero muy cercano al comienzo
    # de la siguiente region, por lo que tomo un valor muy aproximado
    #limite_x5 = [[0,0.719999999999999999],
    #          [0.72,0.829999999999999999],
    #          [0.83,0.899999999999999999],
    #          [0.9,0.949999999999999999],
    #          [0.95,1]]

    limite_x5 = [[0,0.72],
              [0.72,0.83],
              [0.83,0.9],
              [0.9,0.95],
              [0.95,1]]

    # Calculo probabilidades de cada estrato
    # Cada estrato es un hipercubo de grado 5 que tiene un hipercubo mas chico dentro
    # por lo que los resto y resulta en el volumen sobre el que se muestrea
    # Quiero calcular la probabilidad (total) de cada uno de esos estratos, para ello
    # realizo la division (vol_hipercubo/vol_total)
    prob = {}
    #aux = 0
    for i in range(5):
        prob[i]=limite_x5[i][1]-limite_x5[i][0]


    delta = 0.05
    varianza = {}
    estimador = {}
    ns = [0,0,0,0,0]

    clase = int(input('(1)Misma cantidad para estratos, (2)Proporcional a su tamaño: '))
    n = int(input('Ingrese cantidad de replicaciones: '))
    if clase == 1:
        for i in range(5):
            ns[i] = math.trunc(n/5)
    else:
        for i in range(5):
            ns[i] = math.ceil(n*prob[i])
    print(ns)
    for i in range(0, 5):
        estimador[i], varianza[i], _ = volumen_funcion(ns[i], 12345+i*55, limite_x5[i])
        #rango[i] = intervalo(math.trunc(n/5), delta, estimador[i], varianza[i])

    varianza_final = 0
    estimador_final = 0
    for i in range(5):
        estimador_final += prob[i]*estimador[i]
        varianza_final += (varianza[i]*prob[i])/ns[i]
    print(f'Estimacion: {estimador_final}. Estimacion varianza de f: {varianza_final}')
