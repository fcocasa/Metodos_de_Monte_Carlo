import math
import random
import time
from scipy.stats import norm

def cono(x,y):
    return 8-(8/0.4)*math.sqrt((x-0.5)**2+(y-0.5)**2)

def volumen(n,semilla):
    s = 0
    t = 0
    random.seed(semilla)
    for j in range(1,n+1):
        x = random.uniform(0,1)    
        y = random.uniform(0,1)
        z = cono(x,y)
        if z<0:
            z = 0
        if j>1:
            t += (1-1/j)*(z-s/(j-1))**2 
        s += z
    estimador = (s/n)
    var_funcion = t/(n-1)
    var_estimador = var_funcion/n
    return estimador,var_funcion,var_estimador

def main():
	while(True):
		print('--------------------------')
		n =input('Ingrese cantidad de replicaciones (o 0 para salir): ')
		n = int(n)
		if n<1:
			break
		semilla =input('Ingrese una semilla: ')
		
		semilla = int(semilla)
		start_time = time.time()
		estimador, _ , _ = volumen(n,semilla)
		tiempos_exec = time.time() - start_time
		print('\n\tVolumen estimado del cono -> {:.7f}'.format(estimador))

		print('\tTiempo ejecucion de la funcion -> {:.6f} segundos\n'.format(tiempos_exec))


if __name__ == "__main__":
    main()