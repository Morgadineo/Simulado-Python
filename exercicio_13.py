"""13) Contar a quantidade de vogais em uma string
Crie uma função que receba uma string como parâmetro e
retorne a quantidade de vogais presentes nessa string.
Considere apenas as vogais "a", "e", "i", "o" e "u",
independentemente de serem maiúsculas ou minúsculas."""


def contarVogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']  # Lista de vogais
    qtde_vogais = 0  # Variavel de suporte

    for letra in string.lower():  # Para cada letra dentro da string em minuscula
        if letra in vogais:  # Verifica se a letra está presenta na lista
            qtde_vogais += 1

    return qtde_vogais


print(contarVogais('Arthur'))
