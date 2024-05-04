def r(x, y):
    return (3 * x) ** 2 + y ** 2

def b(x, y):
    return 2 * (x ** 2) + (5 * y) ** 2

def c(x, y):
    return -100 * x + y ** 3


def determinar_vencedor(x, y):
    resultado_r = r(x, y)
    resultado_b = b(x, y)
    resultado_c = c(x, y)
    
    if resultado_r > resultado_b and resultado_r > resultado_c:
        return "Rafael ganhou"
    elif resultado_b > resultado_r and resultado_b > resultado_c:
        return "Beto ganhou"
    else:
        return "Carlos ganhou"


N = int(input())


for _ in range(N):
    x, y = map(int, input().split())
    print(determinar_vencedor(x, y))
