def funcion_grado5(x1,x2,x3,x4,x5):
    return x1*(x2**2)*(x3**3)*(x4**4)*(x5**5)

def volumen_funcion(n,semilla):
    s = 0
    t = 0
    random.seed(semilla)
    for j in range(1,n+1):
        x1 = random.uniform(0,1)    
        x2 = random.uniform(0,1)
        x3 = random.uniform(0,1)
        x4 = random.uniform(0,1)
        x5 = random.uniform(0,1)
        z = funcion_grado5(x1,x2,x3,x4,x5)
        if j>1:
            t += (1-1/j)*((z-s/(j-1))**2) 
        s += z
    estimador = (s/n)
    var_funcion = t/(n-1)
    var_estimador = var_funcion/n
    return estimador,var_funcion,var_estimador

def intervalo(n,delta,estimador,var):
    term1 = norm.ppf(1-delta/2)
    term2 = math.sqrt(var_estimador/n)
    return [estimador-term1*term2,estimador+term1*term2]

def valor_n(delta,eps,var):
    term1 = norm.ppf(1-delta/2)**2
    return math.ceil((term1*var)/(eps**2))