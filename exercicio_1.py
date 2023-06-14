"""1) Verificar se um número é primo
Crie uma função que receba um número como parâmetro e
determine se ele é primo ou não. Um número primo é aquele
que é divisível apenas por 1 e por ele mesmo.
"""


def ehPrimo(numero):  # Função em Python

    multiplicadores = 0  # Variável para armazenar os multiplicadores

    if numero <= 1:  # Verifica se o numero é menor ou igual a 1
        return False

    for i in range(2, numero):    # Para cada "i" dentro de um range de 2 até o número
        if numero % i == 0:       # Se o resto da divisão for 0
            multiplicadores += 1  # Adiciona 1 ao multiplicador

    if multiplicadores == 0:  # Se o multiplicador for igual a 0
        return True  # Retorna verdadeiro.
    else:  # Se não
        return False  # Retorna falso


print(ehPrimo(23))  # Printa a chamada da função passando 23 como argumento
