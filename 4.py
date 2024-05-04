def calcular_dias_comida(comida):
    dias = 0
    while comida > 1:
        comida /= 2
        dias += 1
    return dias

N = int(input("Digite o número de casos de teste: "))

for _ in range(N):

    comida = float(input())
    
    dias = calcular_dias_comida(comida)
    print(f"{dias} dias")
