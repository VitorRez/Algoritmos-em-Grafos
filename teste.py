#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph.Read_Ncol("exemplos_conectividade.ncol", directed = False)

plot(g)

s = 0
t = 10
caminho = g.get_all_simple_paths(s,t)
while caminho:

    g.vs['rotulo'] = 0

    for c in caminho:
        for vertice in c:
            g.vs[vertice]['rotulo'] += 1

    maior = -1
    imaior = -1
    for a in g.vs():
        if a.index != s and a.index != t:
            if a['rotulo'] > maior:
                maior = a['rotulo']
                imaior = a.index

    g.delete_vertices(g.vs(imaior))

    for b in g.vs():
        if b['name'] == 's':
            s = b.index
        if b['name'] == 't':
            t = b.index

    caminho = g.get_all_simple_paths(s,t)

plot(g)