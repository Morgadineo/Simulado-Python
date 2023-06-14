"""11) Converter temperatura
Crie uma função que receba uma temperatura em graus
Celsius como parâmetro e a converta para Fahrenheit. A
fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32."""


def celciusFahrenheit(graus):
    return (graus * 9 / 5) + 32  # Formula de Celcius para Fahrenheit


print(celciusFahrenheit(22))
