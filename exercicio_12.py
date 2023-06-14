"""12) Verificar se um número é um quadrado perfeito
Crie uma função que receba um número como parâmetro e
determine se ele é um quadrado perfeito.Um quadrado perfeito
é um número inteiro cuja raiz quadrada também é um número
inteiro.Por exemplo, 25 é um quadrado perfeito porque a sua
raiz quadrada é 5, um número inteiro."""


def ehQuadradoPerfeito(numero):
    numero = int(numero)  # Transforma o número para inteiro
    raiz_quadrada = int(numero ** 0.5)  # Pega a raiz quadrada transformada em inteiro

    if raiz_quadrada ** 2 == numero:  # Aleva o resultado da raiz por 2 e verifica se é igual ao numero
        return True
    else:
        return False


print(ehQuadradoPerfeito(25))
