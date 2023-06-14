"""2) Inverter uma string
Crie uma função que receba uma string como parâmetro e
retorne uma nova string com os caracteres invertidos. Por
exemplo, se a string fornecida for "Hello", a função deve
retornar "olleH"."""


def inverterString(string):
    return string[::-1]  # A forma mais simples


inverterString('Arthur')


def inverterString2(string):  # Forma iterativa
    string_invertida = ""

    for i in range(len(string)):  # Para i no range tamanho da string:
        string_invertida += string[-(i + 1)]  # -(i + 1) Aumenta o i em um, pois -0 é o primeiro item.

    return string_invertida  # Retorna a string_invertida


print(inverterString2('Arthur'))
