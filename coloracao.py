#!/usr/bin/env python
# -*- coding: utf8 -*-

from igraph import *

g = Graph.Read_Ncol("exemplos_conectividade.ncol", directed=False)
g.es['cores'] = 0

color_list = ['azul', 'verde', 'vermelho', 'amarelo', 'roxo', 'rosa', 'cinza', 'preto', 'branco']

for v in g.vs():
    e = g.es.select(_source=v.index)
    cor = 1
    for c in e:
        v_t = c.target
        e_t = g.es.select(_source=v_t)
        v_s = c.source
        e_s = g.es.select(_source=v_s)
        for c_t in e_t:
            if cor == c_t['cores']:
                cor += 1
        for c_s in e_s:
            if cor == c_s['cores']:
                cor += 1
        if c['cores'] == 0:
            c['cores'] = cor
            cor += 1

for v in g.es():
    v['cores'] = color_list[v['cores']]
    print(v.source, v.target, ">", v['cores'])

plot(g, vertex_label = [v.index for v in g.vs()], edge_labels = [es['cores'] for es in g.es()])
    