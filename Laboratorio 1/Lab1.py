import numpy as np
from numpy.random import uniform
import time
import math


def mejor_camino(nodos):
    base = nodos[0] + nodos[9] #T10<-...<-T1
  
    c1 = nodos[7] + max(nodos[3:6]) + nodos[2]
    c2 = nodos[7] + max(nodos[3:5]) + nodos[1]
    c3 = nodos[8] + nodos[4] + max(nodos[2],nodos[1])

    return base + max(c1,c2,c3)


def monte_carlo(t,n):
    esp = 0
    var = 0
    des_media = 0
    
    np.random.seed(12345)
    for i in range(0,n):
        caminos = []
        
        for j in range(0,10):
            valor = np.random.uniform(t[j][0],t[j][1])
            caminos = np.append(caminos,valor)
        valor = mejor_camino(caminos)
        esp += valor
        var += valor*valor
        
    esp = esp/n
    var = var/(n*(n-1)) - (esp*esp)/(n-1)
    des_media = math.sqrt(var)
    return esp, var, des_media


def main():
	tiempos = [[40,56],[24,32],[20,40],[16,48],[10,30],[15,30],[20,25],[30,50],[40,60],[8,16]]

	while (True):
		print('\n-----------------------------------------------------------------------------------------')
		n = input("\n\tEscriba la cantidad de replicaciones que desea realizar (o 1 para salir): ")
		n = int(n)
		if(n<=1):
			break
		start_time = time.time()
		e,v,dm = monte_carlo(tiempos,n)
		tiempos_exec = time.time() - start_time

		print('''\n\tEsperanza -> {:.3f} horas
	Desviacion Media -> {:.7f} horas\n'''.format(e,v,dm))

		print('''\tTiempo ejecucion de la funcion -> {:.4f} segundos\n'''.format(tiempos_exec))

if __name__ == "__main__":
    main()