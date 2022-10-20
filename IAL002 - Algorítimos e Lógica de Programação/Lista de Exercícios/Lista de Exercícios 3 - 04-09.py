# 01
# nota = float(input('Digite uma nota de 0 a 10: '))
# while nota < 0 or nota > 10:
#     print('Comando Inválido!')
#     nota = int(input('Digite uma nota de 0 a 10: '))
# print('Obrigado!')

# 02
# nome = input('Digite o Usuário: ')
# senha = input('Digite a Senha: ')
# while nome == senha:
#     print('O Usuário deve ser DIFERENTE da Senha!')
#     nome = input('Digite o Usuário: ')
#     senha = input('Digite a Senha: ')
# print('Obrigado')

# 03
# a = 80000
# b = 200000
# cont = 0
# while a < b:
#     cont += 1
#     a += a * (3/100)
#     b += b * (1.5/100)
# print(f'Após {cont} anos, a População de A ultrapassou B!')

# 04 # Esse foi complicado
# 1 - 1 - 2 - 3 - 5 - 8
# x = int(input('Qual dígito da sequência deseja mostrar? '))
# a, b = 1, 1
# cont = 0
# while cont < x:
#     cont += 1
#     if x == cont:
#         print(a)
#     a, b = b, (a + b)

# 05
# a = int(input('Digite um número inteiro positivo: '))
# b = int(input('Digite outro: '))
# while a % b != 0:
#     a, b = b, a % b
# print(f'O Máximo Divisor Comum é {b}')
