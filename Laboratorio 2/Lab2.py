import random
import time
import math
from scipy.stats import norm

def muestreo_hoeffding(epsilon,delta):
    return math.ceil((2*math.log(2/delta))/(2*(epsilon**2)))

def muestreo_teo_central(epsilon,delta):
    return math.ceil((norm.ppf(1-delta/2)/(2*epsilon))**2)

def muestreo_chebyshev(epsilon,delta):
    return math.ceil(1/(4*delta*(epsilon**2)))

def pertenece(elemento,centro,radio):
    r_2 = radio*radio
    suma = 0
    for i in range(0,6):
        suma += (elemento[i] - centro[i])*(elemento[i] - centro[i])
        if(suma>r_2):
            return False
    return True

def area(n):
    punto = [0,0,0,0,0,0]
    centro = [0.45,0.5,0.6,0.6,0.5,0.45]
    radio = 0.35
    s = 0
    des_med = 0
    for i in range(0,n):
        # sorteo 1 y 4
        punto[0] = random.uniform(0,1)
        punto[3] = random.uniform(0,1)
        if (3*punto[0] + 7*punto[3] <= 5):
            # sorteo 3
            punto[2] = random.uniform(0,1)
            if (punto[3] + punto[2] <= 1):
                # sorteo el resto
                punto[1] = random.uniform(0,1)
                punto[4] = random.uniform(0,1)
                punto[5] = random.uniform(0,1)
                if(punto[0]-punto[1]-punto[4]+punto[5]>=0 and pertenece(punto,centro,radio)):
                    s +=1
    esp = s / n
    des_med = math.sqrt((s/n)*(1-s/n)/(n-1))
    return [esp,des_med]


def main():
    while (True):
        print('\n-----------------------------------------------------------------------------------------')
        n = input("\n\tEscriba la cantidad de replicaciones que desea realizar (o 0 para salir): ")
        n = int(n)
        if(n<=1):
            break
        random.seed(12345)
        start_time = time.time()
        valores = area(n)
        tiempos_exec = time.time() - start_time

        print('''\n\tEsperanza -> {:.7f}
    Desviacion Media -> {:.7f}\n'''.format(valores[0],valores[1]))

        print('''\tTiempo ejecucion de la funcion -> {:.2f} segundos\n'''.format(tiempos_exec))

if __name__ == "__main__":
    main()