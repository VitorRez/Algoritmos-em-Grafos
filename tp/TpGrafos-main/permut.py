#Essa função gera um dos possíveis caminhos do grafo
import random

def permut(tam):
  part = []

  for i in range(0, tam):
    x = random.randrange(0, tam)
    while x in part:
       x = random.randrange(0, tam)
    part.append(x)
    
  #Acho q é melhor tirar isso
  #part.append(part[0]) #retorna para o vertice inicial

  return part