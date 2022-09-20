#!/usr/bin/env python
# -*- coding: utf8 -*-

from pickle import TRUE
from igraph import *

g = Graph.Read_Ncol("exemplos_caminho.ncol", weights='if_present', directed=True)

rot = []
d = []

for i in g.vs:
        d.append(10000000000.0)
        rot.append(0)
d[0] = 0.0


E = [] 
for i in g.vs():
    s = g.neighbors(i, mode='out')
    for j in s:
        E.append([i.index, j])

print(E)

teste = []

k = 0
while teste != d:
    teste = d.copy()
    vr = g.vs[k]


