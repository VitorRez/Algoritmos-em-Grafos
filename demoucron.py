#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph.Read_Ncol("pert_grafo.ncol", weights='if_present', directed=True)
cont = g.vcount()
g.vs['nivel'] = 0

vi = []
viaux = []
for i in g.vs:
    vi.append(g.neighborhood(i.index, order = cont, mode='in'))
    vi[i.index].remove(i.index)
#plot(g, vertex_label = [v.index for v in g.vs()])
print(vi)

id = 0
nivel = 0
aux = []
cont = 0

for i in g.vs:
        id = 0
        for j in vi:
            if len(j) == 0:
                id = vi.index(j)
                aux.append(id)
                g.vs[id]['nivel'] = nivel
                j.append(-1)
        print(aux)
        for j in vi:
            for m in aux:
                for l in j:
                    if l == m:
                        j.remove(l)
        aux = []
        nivel += 1
        cont += 1


print(g.vs['nivel'])


        
        
        





