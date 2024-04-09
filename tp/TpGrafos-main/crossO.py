#Essa função realiza o crossing over
import random

def crossO(tam, p1, p2):
  #Precisa arrumar?

  f1 = [-1 for i in range(0, tam)]
  f2 = [-1 for i in range(0, tam)]

  x = random.randrange(1, tam-1, 1)
  y = random.randrange(1, tam-1, 1)
  while x == y:
    y = random.randrange(1, tam-1, 1)

  #print(x, y)

  if x > y:
    w1 = x
    w2 = y
  else:
    w1 = y
    w2 = x
  

  qFalta = tam
  for i in range(w2, w1+1):
      f2[i] = p1[i]
      qFalta -= 1
  
  z1 = w1 + 1
  if z1 >= tam:
    z1 = tam-1

  z2 = z1
  while qFalta > 0:
    if not(p2[z1] in f2):
      f2[z2] = p2[z1]
      qFalta -= 1
      
      if z2 >= tam-1:
        z2 = 0
      else:
        z2 += 1

    if z1 >= tam-1:
      z1 = 0
    else:
      z1 += 1
    
  #cria o f1
  qFalta = tam
  for i in range(w2, w1+1):
    f1[i] = p2[i]
    qFalta -= 1

  z1 = w1 + 1
  if z1 >= tam:
    z1 = tam-1

  z2 = z1
  while qFalta > 0:
    if not(p1[z1] in f1):
      f1[z2] = p1[z1]
      qFalta -= 1
    
      if z2 >= tam-1:
        z2 = 0
      else:
        z2 += 1

    if z1 >= tam-1:
      z1 = 0
    else:
      z1 += 1
    
  #Tratamento
  if -1 in f1:
    print("Elemento faltando!")
    print(x, y)
    print(f1)
  if -1 in f2:
    print("Elemento faltando!")
    print(x, y)
    print(f2)

  return f1, f2