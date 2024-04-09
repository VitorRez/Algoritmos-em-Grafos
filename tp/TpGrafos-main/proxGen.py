#Função que pega os 10 melhores dentre os filhos e os 10 melhores entre os pais da gen passada e junta com mais 20 individuos aleatorios
from calcDist import calcDist
from permut import permut

def proxGen(v, filhos, matriz, tam):
  dist = []
  dist2 = []
  p = []
  f = []
  alet = []
  gen = []

  for i in v:
    x = calcDist(matriz, i, tam)
    dist.append(x)
  
  for i in filhos:
    x = calcDist(matriz, i, tam)
    dist2.append(x)

  for i in range(10):
    x = min(dist)
    y = min(dist2)
    p.append(v[dist.index(x)])
    f.append(filhos[dist2.index(y)])
    dist.remove(x)
    dist2.remove(y)

  for i in range(20):
    c = permut(tam)
    while c in p or c in f or c in alet:
      c = permut(tam)
    alet.append(c)

  gen.append(p)
  gen.append(f)
  gen.append(alet)
  
  return gen
