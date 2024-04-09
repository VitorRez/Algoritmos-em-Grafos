#calcula a distancia pelo vetor

def calcDist(matriz, vet, tam): #calcula a distancia pelo vetor
  dist = 0
  for i in range(tam):
    j  = i+1
    if j >= tam:
      break

    dist += matriz[vet[i]][vet[j]]
  dist += matriz[vet[tam-1]][vet[0]]

  return dist
