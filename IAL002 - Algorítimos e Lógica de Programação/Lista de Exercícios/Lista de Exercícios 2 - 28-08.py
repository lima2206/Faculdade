# 01
# a = int(input('Digite o tamanho do primeiro segmento de reta: '))
# b = int(input('Do segundo: '))
# c = int(input('Do terceiro: '))
# if (a + b) > c and (a + c) > b and (b + c) > a:
#     if a == b and b == c:
#         tipo = 'EQUILÁTERO'
#     if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
#         tipo = 'ISÓSCELES'
#     if a != b and a != c and b != c:
#         tipo = 'ESCALENO'
#     print(f'Com os valores informados, é possivel construir um triângulo {tipo}!')
# else:
#     print('Com os valores informados, NÃO é possivel construir um triângulo!')

# 02
# ano = int(input('Qual ano deseja analizar? '))
# if (ano % 4) == 0:
#     if (ano % 100) != 0 or (((ano % 100) == 0) and (ano % 400) == 0):
#         print(f'O ano {ano} É BISSEXTO!')
# else:
#     print(f'O ano {ano} NÃO É BISSEXTO!')

# 03
# peso = int(input('Insira o peso dos peixes em Kg: '))
# excesso = 0
# multa = 0
# if peso > 50:
#     excesso = peso - 50
#     multa = excesso * 4
# print(f'Você está levando {peso}Kg com excesso de {excesso}Kg acima do permitido e sua multa será de R${multa:.2f}!')

# 04
# a = int(input('Digite um número: '))
# b = int(input('Digite outro: '))
# c = int(input('Agora outro: '))
# maior = a
# if b > a and b > c:
#     maior = b
# elif c > a and c > b:
#     maior = c
# print(f'O maior número é o {maior}')

# 05
# a = int(input('Digite um número: '))
# b = int(input('Digite outro: '))
# c = int(input('Agora outro: '))
# maior = a
# menor = b
# if b >= a and b >= c:
#     menor = maior
#     maior = b
#     if c =< menor:
#         menor = c
# if c => a and c => b:
#     menor = maior
#     maior = c
#     if b =< menor:
#         menor = b
# if c < menor:
#     menor = c
# print(f'O maior número é {maior} e o menor {menor}')

# 06
# money = float(input('Digite quanto você ganha por HORA: '))
# tempo = int(input('Digite quantas horas você trabalha no MES: '))
# sal = money * tempo
# print(f'''
# Salário Bruto: R${sal:.2f}
# -IR(11%): R${sal * (11/100):.2f}
# -INSS(8): R${sal * (8/100):.2f}
# -Sindicato(5%): R${sal * (5/100):.2f}
# = Salário Líquido: R${sal - (sal * (24/100)):.2f}
# ''')

# 07
# area = int(input('Diga o tamanho em m² a serem pintados: '))
# litro = area / 3
# latas = litro / 18
# if litro % 18 != 0:
#     latas += 1
# latas = int(latas)
# print(f'Para sua área de {area} m² você precisará de {latas} latas de tinta, totalizando R${latas * 80:.2f}!')
