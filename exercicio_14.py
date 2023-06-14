"""14) Verificar se um número é um número primo de
Fibonacci
Crie uma função que receba um número como parâmetro e
determine se ele é um número primo de Fibonacci.Um número
primo de Fibonacci é um número que é simultaneamente um
número primo e um número da sequência de Fibonacci."""


def ehPrimo(numero):
    multiplicadores = 0  # Variável para armazenar os multiplicadores

    if numero <= 1:  # Verifica se o numero é menor ou igual a 1
        return False

    for i in range(2, numero):  # Para cada "i" dentro de um range de 2 até o número
        if numero % i == 0:  # Se o resto da divisão for 0
            multiplicadores += 1  # Adiciona 1 ao multiplicador

    if multiplicadores == 0:  # Se o multiplicador for igual a 0
        return True  # Retorna verdadeiro.
    else:  # Se não
        return False  # Retorna falso


def ehPrimoFibonacci(numero):
    sequencia_fibonacci = [0, 1, 1]

    num_1 = 0
    num_2 = 1
    num_3 = 1

    for i in range(20):
        num_1 += num_2
        num_2 += num_3
        num_3 = num_1 + num_2
        sequencia_fibonacci.append(num_2)  # Adiciona o numero na lista
        sequencia_fibonacci.append(num_3)  # Adiciona o outro numero na lista
    if (ehPrimo(numero)) and (numero in sequencia_fibonacci):  # Se o numero é primo e está na sequencia
        return True
    else:  # Se não
        return False


print(ehPrimoFibonacci(3))  # Reaproveitei a função da questão 1...
