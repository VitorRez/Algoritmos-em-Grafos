#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

def floyd_warshall(g, D, rotas):
    rx = [] #rota auxiliar
    dx = [] #distancia auxiliar

    for i in g.vs():
        for j in g.vs():
            if i.index == j.index:
                dx.append(0.0)
                rx.append(0)
            else:
                if g.are_connected(i.index, j.index) == True:
                    dx.append(g.es.select(_source=i.index, _target=j.index)['fluxo'][0])
                    rx.append(i.index)
                else:
                    rx.append(0)
                    dx.append(10000000000.0)
        D.append(dx)
        rotas.append(rx)
        rx = []
        dx = []

    print(rotas)

    for k in g.vs():
        for i in g.vs():
            for j in g.vs():
                if D[i.index][k.index] + D[k.index][j.index] < D[i.index][j.index]:
                    D[i.index][j.index] = D[i.index][k.index] + D[k.index][j.index]
                    rotas[i.index][j.index] = rotas[k.index][j.index]
                    

    print(D)
    print(rotas)


#g = Graph.Read_Ncol("exemplos_caminho.ncol", weights='if_present', directed=True)
#rotas = []
#D = []
#floyd_warshall(g, D, rotas)