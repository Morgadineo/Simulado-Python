"""5) Contar a frequência de elementos em uma matriz
Crie uma função que receba um vetor como parâmetro e
retorne um objeto contendo a frequência de cada elemento
presente no vetor. Por exemplo, se o vetor fornecido for [1, 2,
2, 3, 1, 1, 4], a função deve retornar {1: 3, 2: 2, 3: 1, 4: 1}"""


def frequenciaVetor(lista):
    frequencia = {}  # Variavel dicionário vazio

    for numero in lista:  # Itera sobre lista
        qtde = 0  # Quantidade = 0
        for repetido in lista:  # Itera novamente sobre a lista porém dessa vez chamando de repetido
            if numero == repetido:  # Se o numero for igual ao repetido
                qtde += 1  # Qtde += 1
        frequencia[numero] = qtde  # Adiciona no dicionário a chave numero e o valor qtde

    return frequencia


lista = [1, 2, 2, 3, 1, 1, 4]
print(frequenciaVetor(lista))
