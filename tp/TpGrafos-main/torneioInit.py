from permut import permut
def torneioInit(tam, matriz):
  v = []
  
  for a in range(20): #Esse range pode ser que aumente
    #a quantidade de "competidores no torneio" pode aumentar
    c1 = permut(tam)
    c2 = permut(tam)

    while c1 == c2:
      #del c2
      c2 = permut(tam)

    #c1 = [0, 12, 1, 14, 8, 4, 6, 2, 11, 13, 9, 7, 5, 3, 10]

    dist1 = 0
    for i in range(0, tam):
      j = i+1
      if j >= tam:
        break

      dist1 += matriz[c1[i]][c1[j]]
    dist1 += matriz[c1[tam-1]][c1[0]]

    dist2 = 0
    for i in range(0, tam):
      j = i+1
      if j >= tam:
        break

      dist2 += matriz[c2[i]][c2[j]]
    dist2 += matriz[c2[tam-1]][c2[0]]


    if dist1 < dist2:
      v.append(c1)
    else:
      v.append(c2)

  return v

#Precisa continuar a fazer essa função