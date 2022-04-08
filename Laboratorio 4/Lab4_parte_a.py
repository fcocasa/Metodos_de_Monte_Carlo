import numpy as np
import math
import random
import time
from scipy.stats import norm

def intervalo_agresti_coull(estimacion_lambda, delta, n):
	z = norm.ppf(1-delta/2)
	centro_wilson = estimacion_lambda*(n/(n+z**2))+0.5*((z**2)/(n+z**2))
	#print((centro_wilson*(1-centro_wilson))/n)
	pivot = z*math.sqrt(abs((centro_wilson*(1-centro_wilson))/n))
	return [centro_wilson - pivot, centro_wilson + pivot]

def matrix_ceros(rows,cols):
    matrix = []
    for i in range(0,rows):
        row = [0] * cols
        matrix.append(row)
    return matrix

def mul_matrix(a,b):
    ret = matrix_ceros(len(a),len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                if a[i][k]*b[k][j] == 1:
                    ret[i][j] = 1 
    return ret

# Parte A
def valida(profs,b):
	for key in profs:
		for i in profs[key]:
			if b[i][key] != 1:
				return False
	return True

def valores_random(est,profs):
	profesores = {}
	for i in range(est):
		p = random.randrange(0, profs)
		if (p in profesores) :
			profesores[p].append(i)
		else:
			profesores[p] = [i]
	return profesores

def traspuesta(X):#no la use
    result = matrix_ceros(len(X[0]),len(X))
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    return result

if __name__ == "__main__":
	with open('sl.txt', 'r') as f:
		sl = [[int(num) for num in line.split(',')] for line in f]
	with open('pl.txt', 'r') as f:
		pl = [[int(num) for num in line.split(',')] for line in f]
	rows_sl, cols_sl = np.shape(sl)
	lp = traspuesta(pl)
	rows_lp, cols_lp = np.shape(lp)
	conexion_est_prof = mul_matrix(sl,lp)
	random.seed(547)

	r = cols_lp**rows_sl

	n = input("\n\tEscriba la cantidad de replicaciones que desea realizar: ")
	n = int(n)
	
	start_time = time.time()
	nc = 0
	
	for i in range(n):
		prof_ests = valores_random(rows_sl,cols_lp)
		if (valida(prof_ests,conexion_est_prof)):
			nc+=1
	esp = (r*nc)/n
	var = (esp*(r-esp))/(n-1)
	des_med = math.sqrt(var)
	inter = intervalo_agresti_coull(esp, 0.05, n)
	tiempos_exec = time.time() - start_time
	print("\n\tEsperanza -> {:.0f}".format(esp))
	print("\tVarianza -> {:.0f}".format(var))
	print("\tDesviacion Media -> {:.0f}".format(des_med))
	print("\tIntervalo Agresti Coull -> [{:.0f}, {:.0f}]".format(inter[0],inter[1]))
	print('\tTiempo ejecucion -> {:.4f} segundos\n'.format(tiempos_exec))


