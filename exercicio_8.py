"""8) Verificar se uma string é um palíndromo
Crie uma função que receba uma string como parâmetro e
determine se ela é um palíndromo. Um palíndromo é uma
palavra, frase ou sequência de caracteres que pode ser lida da
mesma forma tanto da esquerda para a direita como da direita
para a esquerda, desconsiderando espaços e pontuações."""


def ehPalindromo(string):
    string_invertida = string[::-1]  # String invertida recebe a string invertida
    if string_invertida == string:  # Compara se a string invertida é igual a string
        return True
    else:
        return False


print(ehPalindromo('ovo'))
