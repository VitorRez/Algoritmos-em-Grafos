#Função que faz o cruzamento entre dois elementos aplicando o crossOver e a mutação
from crossO import crossO
from mutacao import mutacao

def cruzamento(v, tam):
  filhos = []
  p = 15 #Valor teste. Mudar depois
  i = 0

  while i < len(v):
    j = i+1
    if j == len(v):
      break

    x = crossO(tam, v[i], v[j])
    filhos.append(x[0])
    filhos.append(x[1])

    i += 2
    
  #print("len = ", len(filhos))
  for a in filhos:
    #talvez precise mudar o valor de p, de forma aleatoria, a cada iteração
    mutacao(a, p)

  return filhos