"""4) Seguindo a lógica do exercício anterior, faça agora um
programa que retorne o maior número, o menor número e a
média aritmética de números de um vetor dado"""

lista = [5, 89, 1, 34, 8, 42, 90, 432, 784, 123, 533, 924, 123, 546, 0, 2]


def maiorElemento(lista):  # Forma iterativa
    maior = 0
    menor = 0

    for numero in lista:  # Para cada número dentro da lista
        if numero > maior:  # Se o número for maior que a variável maior
            maior = numero  # Maior recebe o numero
        elif numero < menor:
            menor = numero

    return (maior + menor) / 2


print(maiorElemento(lista))


def maiorElemento2(lista):  # Forma simples
    lista.sort()  # Ordena a lista em ordem crescente
    maior = lista[-1]  # Pega o ultimo valor
    menor = lista[0]  # Pega o primeiro valor
    return (maior + menor) / 2


print(maiorElemento2(lista))
