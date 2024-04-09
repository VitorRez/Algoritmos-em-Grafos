#Essa função faz o torneio para conseguirmos os 20 melhores para o cruzamento"""

def torneio(gen, matriz, tam):
  v = []
  for a in range(20):
    b = a+1
    dist1 = 0
    dist2 = 0
    for i in range(tam):
      j = i+1
      if j >= tam:
        break
      dist1 += matriz[gen[a][i]][gen[a][j]]
      dist2 += matriz[gen[b][i]][gen[b][j]]
    dist1 += matriz[gen[a][tam-1]][gen[a][0]]
    dist2 += matriz[gen[b][tam-1]][gen[b][0]]

    if dist1 <= dist2:
      v.append(gen[a])
    else:
      v.append(gen[b])
    
  return v
