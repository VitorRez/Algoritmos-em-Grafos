#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph.Read_Ncol("exemplos_caminho.ncol", weights='if_present', directed=True)

A   =   []
d   =   []
f   =   []
rot =   []
s   =   []

for i in g.vs:
        d.append(0.0)
        rot.append(0)
        A.append(i.index)
d[0] = 0.0

j = 0
while A:
    vr = g.vs[j]
    A.remove(vr.index)
    f.append(vr.index)
    s = set(g.neighbors(vr, mode='out')) & set(A)
    for i in s:
        p = min(d[vr.index] + g.es.select(_source=vr.index, _target=i)['weight'][0], d[i])
        if p > d[i]:
            d[i] = p
            rot[i] = int(vr['name'])
    j = j + 1

print(d)
print(rot)