from math import log
from math import factorial
n = 1
lista = []


while n != 0:
    n = int(input('Digite n: '))
    if n == 0:
        break
    logarit = round(log(n, 2))
    quadrado = n ** 2
    elev = str(2 ** n)
    fact = str(factorial(n))
    lista.append(f'{logarit}|{n}|{quadrado}|{len(elev)}dig|{len(fact)}dig')


for c in lista:
    print(c)