"""9) Calcular fatorial de um número
Crie uma função que receba um número como parâmetro e
retorne o fatorial desse número. O fatorial de um número é o
produto de todos os números inteiros positivos menores ou
iguais a ele. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 =
120."""


def fatorial(numero):  # Função recursiva
    if numero == 1:
        return 1
    else:
        return fatorial(numero - 1) * numero


print(fatorial(5))
