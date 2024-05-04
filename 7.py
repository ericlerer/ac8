def contar_vitorias(resultados):
    vitorias_maria = resultados.count(0)
    vitorias_joao = resultados.count(1)
    return vitorias_maria, vitorias_joao


while True:

    N = int(input())
    

    if N == 0:
        break
    

    resultados = list(map(int, input().split()))
    
  
    vitorias_maria, vitorias_joao = contar_vitorias(resultados)
    
 
    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")
