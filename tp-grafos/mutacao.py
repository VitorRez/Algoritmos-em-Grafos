from random import randint

#essa função vai tratar vetor por vetor, por isso a entrada é um vetor no lugar da matriz com todos os filhos
#V = vetor com a permutação de vertices
#p = probabilidade de ocorrer a mutação em determinado vertices, p é um valor de 0 a 100
def mutacao(v, p):

    for i in v:
        x = randint(0, 100)
        if x <= p:
            posicao_atual = v.index(i)
            posicao = randint(0, len(v))
            while posicao == posicao_atual:
                posicao = randint(0, len(v))
            aux = v[posicao]
            v[posicao] = v[posicao_atual]
            v[posicao_atual] = aux

