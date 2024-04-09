#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph([(0,1),(0,3),(1,2),(2,5),(3,4),(3,2),(4,5)], directed = True)
g.es()['custo'] = [20,10,30,20,15,10,20]
g.es()['fluxo'] = [50,40,60,30,60,70,50]
g.vs()['nome'] = ['s', 'a', 'b', 'c', 'd','t']

plot(g, vertex_label = [v.index for v in g.vs()], edge_labels = [es['fluxo'] for es in g.es()])

gf = g
paths = g.get_all_simple_paths(0, 5)
paths_p = []
mins = []
for i in paths:
    aux = []
    for j in i:
        k = i.index(j)
        if k+1 < len(i):
            aux.append(g.es.select(_source=j, _target=i[k+1])['fluxo'][0])
    paths_p.append(aux)

for i in paths_p:
    mins.append(min(i))

print(mins)
print(paths_p)        
print(paths)

id = 0
for i in paths:
    for j in range(len(i)):
        if j+1 < len(i) and id < len(mins):
            if g.es.select(_source=i[j], _target=i[j+1])['fluxo'][0] > mins[id]:
                g.es.select(_source=i[j], _target=i[j+1])['fluxo'][0] += mins[id]
                g.add_edge(i[j+1], i[j])
                g.es.select(_source=i[j+1], _target=i[j])['fluxo'][0] = mins[id]
            if g.es.select(_source=i[j], _target=i[j+1])['fluxo'][0] == mins[id]:
                g.delete_edges(i[j], i[j+1])
                g.es.select(_source=i[j+1], _target=i[j])['fluxo'][0] += mins[id]
            if g.es.select(_source=i[j+1], _target=i[j])['fluxo'][0] == mins[id]:
                g.delete_edges(i[j+1], i[j])
                g.es.select(_source=i[j], _target=i[j+1])['fluxo'][0] += mins[id]
        j += 1
    plot(g, vertex_label = [v.index for v in g.vs()], edge_labels = [es['fluxo'] for es in g.es()])
    id += 1
        



#
#cap_corte = 10000000
#f0 = 0
#s = 0 
#t = 5
#while cap_corte != f0:
#    gf = g
#    paths = gf.get_all_simple_paths(s,t)
#
    