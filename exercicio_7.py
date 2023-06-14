"""7) Remover elementos duplicados de uma matriz
Crie uma função que receba uma matriz como parâmetro e
retorne uma nova matriz sem elementos duplicados. Por
exemplo, se a matriz fornecida for [1, 2, 2, 3, 1, 4], a função
deve retornar [1, 2, 3, 4]."""


def removerDuplicado(lista):
    lista_2 = set(lista)  # Transforma a lista em set.
    lista_2 = list(lista_2)  # Transforma o set de volta pra lista
    return lista_2  # Retorna a lista sem elementos duplicados


lista = [1, 2, 2, 3, 1, 4]
print(removerDuplicado(lista))
