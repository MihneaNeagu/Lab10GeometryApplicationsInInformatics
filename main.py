import math as mat
import os
from geomdl import NURBS
from geomdl import utilities
from geomdl.visualization import VisMPL

def combinari(n, k):
    return mat.factorial(n) / (mat.factorial(k) * mat.factorial(n - k))

def B(n, k, t):
    return combinari(n, k) * mat.pow(t, k) * mat.pow(1 - t, n - k)

def puncte_de_control(n):
    a = []

    for index in range(n):
        print("punctul", index)
        x = float(input("x = "))
        y = float(input("y = "))
        a.append((x, y))

    return a

def ponderi(n):
    w = []

    for index in range(n):
        print("ponderea", index)
        a = float(input("w = "))
        w.append(a)

    return w




def punct_k(lista, k):
    return lista[k - 1]


def curba_bezier(n, t, puncte, pond):
    curba_x = 0
    curba_y = 0

    for k in range(n):
        p = punct_k(puncte, k)
        curba_x += (pond[k] * B(n, k, t) * p[0])/(pond[k] * B(n,k,t))
        curba_y += (B(n, k, t) * p[1])/(pond[k] * B(n,k,t))

    return curba_x, curba_y




def main():
    n = 4
    puncte = puncte_de_control(n)
    pond = ponderi(n)
    t = float(input("Da-ti un t de la 0 la 1 : "))
    r = curba_bezier(n, t, puncte, pond)
    print("r(", t, ") = ", r)

main()