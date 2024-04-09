#Essa função acha o melhor caminho dentro todos da geração e devolve a distancia e o caminho
from calcDist import calcDist

def achaMelhor(v, matriz, tam):
  vDist = []
  for i in v:
    vDist.append(calcDist(matriz, i, tam))
  
  melhor = min(vDist)
  return melhor, vDist.index(melhor)
