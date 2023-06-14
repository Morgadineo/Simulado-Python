"""3) Encontrar o maior elemento em um vetor
Crie uma função que receba uma matriz de números como
parâmetro e retorne o maior elemento presente nesse vetor."""

lista = [5, 89, 1, 34, 8, 42, 90, 432, 784, 123, 533, 924, 123, 546, 0, 2]


def maiorElemento(lista):  # Forma iterativa
    maior = 0

    for numero in lista:  # Para cada número dentro da lista
        if numero > maior:  # Se o número for maior que a variável maior
            maior = numero  # Maior recebe o numero

    return maior  # Retorna o número


print(maiorElemento(lista))


def maiorElemento2(lista):  # Forma simples
    lista.sort()  # Ordena a lista em ordem crescente
    return lista[-1]  # Retorna o ultimo valor da lista


print(maiorElemento2(lista))
