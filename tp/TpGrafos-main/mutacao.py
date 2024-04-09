from random import randint

#essa função vai tratar vetor por vetor, por isso a entrada é um vetor no lugar da matriz com todos os filhos
#V = vetor com a permutação de vertices
#p = probabilidade de ocorrer a mutação em determinado vertices, p é um valor de 0 a 100
def mutacao(v, p):
  #print("antes", v)
  
  for i in v:
    x = randint(0, 100)
    #print(x)
    if x <= p: #Pq <= ?
      #print("Entrou")
      posicao_atual = v.index(i)
      posicao = randint(0, len(v))
      while posicao == posicao_atual or posicao == len(v):
          posicao = randint(0, len(v))
      #print(posicao, posicao_atual)
      #print(v)
      aux = v[posicao]
      v[posicao] = v[posicao_atual]
      v[posicao_atual] = aux

  #print("depois", v)