#Essa função retorna um vetor com todos os participantes do torneio posicionados de uam forma "aleatoria"

def ordena(gen):
  p = 0
  f = 0
  alet = 0
  i = 0
  v = []

  for i in range(40):
    if i % 2 == 0:
      if p <= f:
        v.append(gen[0][p])
        p += 1
      else:
        v.append(gen[1][f])
        f += 1
    else:
      v.append(gen[2][0])
      alet += 1

  return v
