import random as rm
import math as m
import time
from statistics import mode
# 1) c)


def permutacion(a):  # a=[a[0],a[1],...,a[N-1]]
    N = len(a)
    for j in range(N-1, 0, -1):
        indice = int((j+1) * rm.random())
        a[j], a[indice] = a[indice], a[j]


def permutacion_cartas():
    a = []
    i = 1
    while i <= 100:
        a.append(i)
        i = i + 1
    permutacion(a)
    return a


def ejercicio1(Nsim):
    res = []
    for _ in range(Nsim):
        a = permutacion_cartas()
        i = 1
        acc = 0
        while i <= 100:
            if a[i - 1] == i:
                acc = acc + 1
            i = i + 1
        res.append(acc)
    media = sum(res) / Nsim
    v = 0
    for j in range(Nsim):
        v = (abs(res[j]-media))**2 + v
    var = v/Nsim
    print("La media es: " + str(media))
    print("La desviacion estandard es: " + str(var))
# Nsim = 1000:
# La media es: 0.9999
# La desviacion estandard es: 0.9928999900000872

# ------------------

# 2)


def ejercio2(Nsim, N):
    Suma = 0
    Nsim = 100
    for _ in range(Nsim):
        U = int(rm.random() * N) + 1
        Suma += m.exp(U / N)
    Suma = Suma / Nsim * N
    return Suma

# b) ejercio2(100, 10000) = 16906.61238888207
# valor exacto = 17183.6774398236971

# c) ejercio2(100, 100) = 169.7366250252624
# valor exacto = 172.68875565927126516

# ------------------

# 3)


def par_de_dados():
    n = 0
    dado = [1, 2, 3, 4, 5, 6]
    a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while True:
        i = rm.choice(dado)
        j = rm.choice(dado)
        a[i+j-2] = 0
        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if a == s:
            return n
        else:
            n = n + 1


def sim_par_de_dados(Nsim):
    i = 0
    a = []
    while i < Nsim:
        a.append(par_de_dados())
        i = i + 1
    media = sum(a) / Nsim
    v = 0
    p15 = 0
    p9 = 0
    for j in range(Nsim):
        v = (abs(a[j]-media))**2 + v
        if a[j] >= 15:
            p15 = p15 + 1
        elif a[j] <= 9:
            p9 = p9 + 1
    p9 = p9/Nsim
    p15 = p15/Nsim
    de = m.sqrt(v/Nsim)
    print("La media es: " + str(media))
    print("La desviacion estandard es: " + str(de))
    print("La probabilidad de que N sea a lo sumo 9 es: " + str(p9))
    print("La probabilidad de que N sea por lo menos 15 es: " + str(p15))
# Nsim = 10000 :
# La media es :59.7749
# La desviacion estandard es :35.32090075281206
# La probabilidad de que N sea a lo sumo 9 es: 0.0
# La probabilidad de que N sea por lo menos 15 es: 0.9975

# ------------------

# 4)
# a)


def ejercicio4_a():
    prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
    c = 0.14/(1/10)
    while True:
        y = rm.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        u = rm.random()
        if u < prob[y]/(c*1/10):
            return y + 1


# b)
def ejercicio4_b():
    u = rm.random()
    if u < 0.14:
        return 2
    elif u < 0.14 + 0.12:
        return 5
    elif u < 0.14 + 0.12:
        return 5
    elif u < 0.14 + 0.12 + 0.11:
        return 1
    elif u < 0.14 + 0.12 + 0.11 + 0.11:
        return 9
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1:
        return 6
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09:
        return 3
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09 + 0.09:
        return 7
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09 + 0.09 + 0.09:
        return 10
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09 + 0.09 + 0.09 + 0.08:
        return 4
    elif u < 0.14 + 0.12 + 0.11 + 0.11 + 0.1 + 0.09 + 0.09 + 0.09 + 0.08 + 0.07:
        return 8


# c)
def ejercicio4_c():
    a = []
    i = 0
    while i < 11:
        a.append(1)
        i = i + 1
    while i < 11 + 14:
        a.append(2)
        i = i + 1
    while i < 11 + 14 + 9:
        a.append(3)
        i = i + 1
    while i < 11 + 14 + 9 + 8:
        a.append(4)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12:
        a.append(5)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12 + 10:
        a.append(6)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12 + 10 + 9:
        a.append(7)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12 + 10 + 9 + 7:
        a.append(8)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12 + 10 + 9 + 7 + 11:
        a.append(9)
        i = i + 1
    while i < 11 + 14 + 9 + 8 + 12 + 10 + 9 + 7 + 11 + 9:
        a.append(10)
        i = i + 1
    return a[int(rm.random()*100)]


# eficiencias por tiempo :
def e4a(Nsim):
    for _ in range(Nsim):
        ejercicio4_a()


def e4b(Nsim):
    for _ in range(Nsim):
        ejercicio4_b()


def e4c(Nsim):
    for _ in range(Nsim):
        ejercicio4_c()


def eficiencias():
    inicio_a = time.time()
    e4a(10000)
    fin_a = time.time()
    print("tiempo a: " + str(fin_a-inicio_a))
    inicio_b = time.time()
    e4b(10000)
    fin_b = time.time()
    print("tiempo b: " + str(fin_b-inicio_b))
    inicio_c = time.time()
    e4c(10000)
    fin_c = time.time()
    print("tiempo c: " + str(fin_c-inicio_c))
# tiempo a: 0.011647701263427734
# tiempo b: 0.002437591552734375
# tiempo c: 0.054524898529052734

# ------------------

# 5)
# i)


def Binomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = rm.random()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i

# ii)


def Binomial2(n, p):
    a = 0
    for _ in range(n):
        if rm.random() < p:
            a = a + 1
    return a

# a)


def bin(Nsim):
    for _ in range(Nsim):
        Binomial(10, 0.3)


def bin2(Nsim):
    for _ in range(Nsim):
        Binomial2(10, 0.3)


def eficiencia5():
    inicio_a = time.time()
    bin(10000)
    fin_a = time.time()
    print("tiempo i: " + str(fin_a-inicio_a))
    inicio_b = time.time()
    bin2(10000)
    fin_b = time.time()
    print("tiempo ii: " + str(fin_b-inicio_b))
# tiempo i: 0.010618448257446289
# tiempo ii: 0.007343292236328125

# b)


def ocurriencias(Nsim):
    a = []
    cero, diez = 0, 0
    for i in range(Nsim):
        a.append(Binomial(10, 0.3))
        if a[i] == 0:
            cero = cero + 1
        elif a[i] == 10:
            diez = diez + 1
    mayorOcurriencia = mode(a)
    n = 0
    for j in range(Nsim):
        if a[j] == mayorOcurriencia:
            n = n+1
    print("se obtubo " + str(mayorOcurriencia) + ": " +
          str(n) + " veces en " + str(Nsim) + " simulaciones")
    print("se obtubo 0: " + str(cero) +
          " veces en " + str(Nsim) + " simulaciones")
    print("se obtubo 10: " + str(diez) +
          " veces en " + str(Nsim) + " simulaciones")


def ocurriencias2(Nsim):
    a = []
    cero, diez = 0, 0
    for i in range(Nsim):
        a.append(Binomial2(10, 0.3))
        if a[i] == 0:
            cero = cero + 1
        elif a[i] == 10:
            diez = diez + 1
    mayorOcurriencia = mode(a)
    n = 0
    for j in range(Nsim):
        if a[j] == mayorOcurriencia:
            n = n+1
    print("se obtubo " + str(mayorOcurriencia) + ": " +
          str(n) + " veces en " + str(Nsim) + " simulaciones")
    print("se obtubo 0: " + str(cero) +
          " veces en " + str(Nsim) + " simulaciones")
    print("se obtubo 10: " + str(diez) +
          " veces en " + str(Nsim) + " simulaciones")

# ------------------

# 6)
# i)


def ej6_i():
    u = rm.random()
    if u < 0.35:
        return 3
    elif u < 0.35 + 0.2:
        return 1
    elif u < 0.35 + 0.2 + 0.2:
        return 4
    elif u < 0.35 + 0.2 + 0.2 + 0.14:
        return 0
    else:
        return 2

# ii)


def prob_binomial(n, p, i):
    return (m.factorial(n)/(m.factorial(i)*(m.factorial(n-i)))) * p**i * (1-p)**(n+1)


def ej6_ii(c):
    probs_x = [0.15, 0.20, 0.10, 0.35, 0.20]
    while True:
        y = Binomial2(4, 0.45)
        prob_y = prob_binomial(4, 0.45, y)
        u = rm.random()
        if u < probs_x[y]/(c*prob_y):
            return y

# ii)


def e6_1(Nsim):
    for _ in range(Nsim):
        ej6_i()


def e6_2(Nsim):
    for _ in range(Nsim):
        ej6_ii(8.64)


def eficiencia6():
    inicio_a = time.time()
    e6_1(10000)
    fin_a = time.time()
    print("tiempo i: " + str(fin_a-inicio_a))
    inicio_b = time.time()
    e6_2(10000)
    fin_b = time.time()
    print("tiempo ii: " + str(fin_b-inicio_b))
# tiempo i: 0.0029664039611816406
# tiempo ii: 0.025534391403198242

# ------------------

# 7)


def Poisson(lamda):
    p = m.exp(-lamda)
    F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
    U = rm.random()
    if U >= F:
        j = int(lamda) + 1
        while U >= F:
            p *= lamda / j
            F += p
            j += 1
        return j - 1
    else:
        j = int(lamda)
        while U < F:
            F -= p
            p *= j/lamda
            j -= 1
        return j+1


def ymayor2(Nsim):
    res = 0
    for _ in range(Nsim):
        if Poisson(0.7) > 2:
            res = res + 1
    return res/Nsim
# ymayor2(1000)
# 0.034

# ------------------

# 8)
# transformada inversa:
# a)


def p_i(lam, k):
    u = rm.random()
    s = 0
    a = []
    for j in range(k):
        s = lam**j/m.factorial(j) * m.exp(-lam) + s
    for i in range(k):
        a.append((lam**i/m.factorial(i) * m.exp(-lam)) / s)

    l = a[0]
    for h in range(k):
        if u < l:
            return h
        else:
            l = l + a[h+1]

# b)


def p_i_n(Nsim):
    res = 0
    for _ in range(Nsim):
        if p_i(0.7, 10) > 2:
            res = res + 1
    return res / Nsim
# p_i_n(10000)
# 0.0345

# rechazo
# a)


def prob_ej8(lam, y, k):
    s = 0
    for j in range(k):
        s = lam**j/m.factorial(j) * m.exp(-lam) + s
    return(lam**y/m.factorial(y) * m.exp(-lam)) / s


def ayr_ej8(lam, k, c):
    y = rm.randint(0, k)
    prob_y = 1/(k+1)
    u = rm.random()
    prob_x = prob_ej8(lam, y, k)
    if u < prob_x/(c*prob_y):
        return y
    else:
        return ayr_ej8(lam, k, c)
# c = 0.4965853058406688 / (1/10) = 4.96

# b)


def p_i_n2(Nsim):
    res = 0
    for _ in range(Nsim):
        if ayr_ej8(0.7, 10, 4.96) > 2:
            res = res + 1
    return res / Nsim
# p_i_n2(1000)
# 0.035

# 9)
# transformada inversa
# a)


def geometrica(p):
    U = rm.random()
    return int(m.log(1-U)/m.log(1-p))+1


def geometrica2(p):
    res = 1
    while True:
        u = rm.random()
        if u < p:
            return res
        res = res + 1

# b)


def l_geo(Nsim, p):
    res = 0
    for _ in range(Nsim):
        res = geometrica(p) + res
    return res / Nsim


def l_geo2(Nsim, p):
    res = 0
    for _ in range(Nsim):
        res = geometrica2(p) + res
    return res / Nsim


# geometrica recursiva:
# a)
def geo_rec(p, n):  # ???????????
    q = (1 - p)
    return p * q**(n-1)

# b)


def l__geo3(Nsim, p):  # ?????????
    res = 0
    for _ in range(Nsim):
        res = geo_rec(p, l_geo2(Nsim, p)) + res
    return res / Nsim


def eficiencia9():
    inicio_a = time.time()
    l_geo(10000, 0.8)
    fin_a = time.time()
    print("tiempo geometrica: " + str(fin_a-inicio_a))
    inicio_b = time.time()
    l_geo2(10000, 0.8)
    fin_b = time.time()
    print("tiempo geometrica2: " + str(fin_b-inicio_b))
    inicio_a = time.time()
    l_geo(10000, 0.2)
    fin_a = time.time()
    print("tiempo geometrica: " + str(fin_a-inicio_a))
    inicio_b = time.time()
    l_geo2(10000, 0.2)
    fin_b = time.time()
    print("tiempo geometrica2: " + str(fin_b-inicio_b))


# 10
def generarxx(k):
    u = rm.random()
    a = [0]
    i = 1
    while i < k + 1:
        a.append((1/2)**(i+1) + ((1/2)*2**(i-1))/(3**i))
        i = i+1
    l = a[0]
    for h in range(k):
        if u < l:
            return h
        else:
            l = l + a[h+1]
    return h


def p_gxx(Nsim):
    res = 0
    for _ in range(Nsim):
        res = generarxx(10) + res
    return res / Nsim
# p_gxx(1000)
# 2.453


# esperanza
a = [0]
i = 1
while i < 10:
    a.append((1/2)**(i+1) + ((1/2)*2**(i-1))/(3**i))
    i = i+1
    res = 0
for i in range(10):
    res = i*a[i] + res
# 2.3331840432575066


def QueDevuelve(p1, p2):
    X = int(m.log(1-rm.random())/m.log(1-p1))+1
    Y = int(m.log(1-rm.random())/m.log(1-p2))+1
    return min(X, Y)


def l_qd(Nsim):
    res = 0
    for _ in range(Nsim):
        res = QueDevuelve(0.05, 0.2) + res
    return res/Nsim

def qdnew(p1,p2):
    res1 = 1
    res2 = 1
    while True:
        u = rm.random()
        if u < p1:
            return res1
        if u < p2:
            return res2
        res1 = res1 + 1
        res2 = res2 + 1
#?
def qdnew(p1,p2):
    res1 = 1
    res2 = 1
    while True:
        u = rm.random()
        if u < p1:
            break
        res1 = res1 + 1
    while True:
        u = rm.random()
        if u < p2:
            break
        res2 = res2 + 1
    return min(res1, res2)

def l_qdnew(Nsim):
    res = 0
    for _ in range(Nsim):
        res = qdnew(0.05, 0.2) + res
    return res/Nsim