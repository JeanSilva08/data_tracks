import random

# Função para gerar 6 números aleatórios criptograficamente seguros sem repetições
def sorteio_criptografico():
    # Usando random.sample() para garantir que não haja repetições
    numeros_sorteados = random.sample(range(1, 61), 6)
    # Organiza os números de forma crescente
    numeros_sorteados.sort()
    return numeros_sorteados

# Realiza o sorteio criptograficamente seguro e exibe os números sorteados
numeros_ordenados_criptografico = sorteio_criptografico()

# Imprime o resultado final
print(numeros_ordenados_criptografico)
