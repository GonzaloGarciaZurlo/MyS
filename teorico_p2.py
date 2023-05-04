import random as rm
import math as m
import matplotlib.pyplot as plt

# x: vector de valores posibles de X
# p: vector de probabilidades
def discretaX(p, x): # metodo de transformada inversa
    U = rm.random()
    i, F = 0, p[0]
    while U >= F:
        i +=1
        F += p[i]
    return x[i]

def discretaX1():
    return discretaX([0.2,0.15,0.25,0.4],[1,2,3,4])

def discretaX1_op():
    return discretaX([0.4,0.25,0.2,0.15,],[4,3,1,2])


def udiscreta(n): # metodo de transformada inversa uniforme
    U = rm.random()
    x = 1; F = 1/n
    while U >= F:
        F += 1 / n
        x += 1
    return x

def udiscreta(n): # metodo de transformada inversa uniforme op
    U = rm.random()
    return int(n * U) + 1

def udiscreta(m,k): # metodo de transformada inversa uniforme op en [m,k]
    U = rm.random()
    return int(U * (k - m + 1)) + m


def permutacion(a): #a=[a[0],a[1],...,a[N-1]]
    N = len(a)
    for j in range(N-1,0,-1):
        indice = int((j+1) * rm.random())
        a[j], a[indice] = a[indice], a[j]

## Devuelve un subconjunto aleatorio de A de r elementos
def subcAleatorio(r,A):
    N = len(A)
    for j in range(N-1, N-1-r, -1):
        indice = int((j+1) * rm.random())
        A[j], A[indice] = A[indice], A[j]
    return A[N-r:]


def geometrica(p):
    U = rm.random()
    return int(m.log(1-U)/m.log(1-p))+1


def Bernoulli(p):
    U=rm.random()
    if U < p: return 1
    else: return 0

##devuelve una lista de N Bernoullis B(p)
def NBernoullis(N,p):
    Bernoullis = [0] * N
    j = geometrica(p)-1
    while j < N:
        Bernoullis[j] = 1
        j += geometrica(p)
    return Bernoulli


def Poisson(lamda):
    p = m.exp(-lamda); F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
    U = rm.random()
    if U >= F:
        j = int(lamda) + 1
        while U >= F:
            p *= lamda / j; F += p
            j += 1
        return j - 1
    else:
        j = int(lamda)
        while U < F:
            F -= p; p *= j/lamda
            j -= 1
        return j+1


def Binomial(n,p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob; i=0
    U = rm.random()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i


