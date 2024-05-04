N = int(input())


contagem = {}

for _ in range(N):
    valor = int(input())
    contagem[valor] = contagem.get(valor, 0) + 1

numeros_ordenados = sorted(contagem.keys())


for numero in numeros_ordenados:
    print(f"{numero} aparece {contagem[numero]} vez(es)")
