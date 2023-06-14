"""10) Verificar se uma palavra é um anagrama
Crie uma função que receba duas palavras como parâmetros e
determine se elas são anagramas. Um anagrama é uma
palavra formada pela transposição das letras de outra palavra.
Por exemplo, as palavras "amor" e "roma" são anagramas."""


def ehAnagrama(string_1, string_2):
    string_1_invertida = string_1[::-1]  # Reverte a string_1 e armazena em uma variavel

    if string_1_invertida == string_2:  # Compara se a string_1 invertida é igual a string_2
        return True
    else:
        return False


print(ehAnagrama('amor', 'roma'))
