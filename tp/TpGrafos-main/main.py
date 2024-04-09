from torneioInit import torneioInit
from criaMatrix import criaMatriz
from cruzamento import cruzamento
from proxGen import proxGen
from ordena import ordena
from torneio import torneio
from achaMelhor import achaMelhor
from calcDist import calcDist

#O melhor caminho para esse grafo é: [0, 12, 1, 14, 8, 4, 6, 2, 11, 13, 9, 7, 5, 3, 10] -> 291
#Se quiser ver os melhores de cada geração é só retirar os comentários

def main():
  matriz = criaMatriz()
  tam = len(matriz)
  melhor = [-1]
  cont = 0
  file1 = open("gen.txt", "w")

  v = torneioInit(tam, matriz)
  #while melhor[0] != 291:
  #for i in range(3000):
  x = 0
  melhor_anterior = 1
  while x < 2500:
    filhos = cruzamento(v, tam)
    gen = proxGen(v, filhos, matriz, tam)
    gen = ordena(gen)
    cont += 1
    v = torneio(gen, matriz, tam)
    melhor = achaMelhor(v, matriz, tam)

    file1.write(str(v[melhor[1]]) + "\n")
    file1.write(str(calcDist(matriz, v[melhor[1]], tam)) + "\n")
    file1.write("--------------------" + "\n")
    if v[melhor[1]] == melhor_anterior:
      x += 1
    else:
      x = 0
      melhor_anterior = v[melhor[1]]
  
  print(v[melhor[1]])
  print(calcDist(matriz, v[melhor[1]], tam))
  print(cont)

  file1.write("O numero de geracoes foi: " + str(cont))

  file1.close()
#-----------------
main()