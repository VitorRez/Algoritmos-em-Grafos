#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph.Read_Ncol("exemplo_arvore.ncol", weights='if_present', directed=False)

F = []
arestaaux = []
taux = []

Ti = g.vs
Tj = g.vs
cont = 1
while len(F) < len(g.es):
    for i in Ti:
        valor = 100000000000
        for j in Tj:
            if j != i:
                if g.are_connected(i.index, j.index) == True:
                    if g.es.select(_source=i.index, _target=j.index)['weight'][0] < valor:
                        valor = g.es.select(_source=i.index, _target=j.index)['weight'][0]
                        arestaaux.append([i.index,j.index])
                        taux.append(j)
        for k in arestaaux:
            if k not in F:
                F.append(k)
        for k in taux:
            if k not in Ti:
                Ti.append(k)
        arestaaux = []
        taux = []
print(F)
                