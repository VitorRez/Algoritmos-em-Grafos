from igraph import *

def criaG(): #Vai ser realamente necessário? Resposta: N, n vai
  g = Graph()
  g = g.Read_Adjacency("lau15_dist.txt", attribute="weights")
  g.vs['name'] = [v.index for v in g.vs()]
  plot(g)

criaG()
