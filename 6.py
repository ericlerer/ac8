import math


def eh_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = int(math.sqrt(numero)) + 1
    for i in range(3, limite, 2):
        if numero % i == 0:
            return False
    return True


N = int(input())


for _ in range(N):
    
    valor = int(input())
    
    
    if eh_primo(valor):
        print("Prime")
    else:
        print("Not Prime")
