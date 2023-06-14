"""6) Validar uma senha
Crie uma função que receba uma senha como parâmetro e
verifique se ela atende aos seguintes critérios: ter pelo menos
8 caracteres, conter pelo menos uma letra maiúscula, uma letra
minúscula e um número."""
import re  # Biblioteca que permite o Python trabalhar com expressões regulares


def validarSenha(senha):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'  # Expressão regular

    if re.match(regex, senha):  # Função da biblioteca re para comparar string com a regex. Retorna True ou False
        print('Senha válida')
    else:
        print('Senha inválida')


validarSenha('Arthur123456')
