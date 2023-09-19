# 01
# n = int(input('Digite um número inteiro não-negativo: '))
# a = 0
# x = 0
# while x < n:
#     a += 1
#     x = a * (a+1) * (a+2)
# if x == n:
#     print(f'O número {n} é triangular, pois {a} x {a+1} x {a+2} = {x} ')
# else:
#     print(f'O número {n} não é triangular.')

# 02 Jeito Ruim sem o While
# x = int(input('Digite o valor a ser sacado: '))
# # resto de divisão para as notas
# x50 = x % 50
# x20 = x50 % 20
# x10 = x20 % 10
# x5 = x10 % 5
# x2 = x5 % 2
# # notas
# nota50 = int(x / 50)
# nota20 = int(x50 / 20)
# nota10 = int(x20 / 10)
# nota5 = int(x10 / 5)
# nota2 = int(x5 / 2)
# nota1 = int(x2)
# print(f'Ao sacar R${x:.2f} você receberá...')
# if nota50 > 0:
#     print(f'{nota50} notas de R$50.00')
# if nota20 > 0:
#     print(f'{nota20} notas de R$20.00')
# if nota10 > 0:
#     print(f'{nota10} notas de R$10.00')
# if nota5 > 0:
#     print(f'{nota5} notas de R$5.00')
# if nota2 > 0:
#     print(f'{nota2} notas de R$2.00')
# if nota1 > 0:
#     print(f'{nota1} notas de R$1.00')
# print('OBRIGADO!')

# 02 Bom com o While
# valor = int(input('Digite quando deseja sacar: '))
# total = valor
# totced = 0
# ced = 50  # valor inicial da cédula
# while True:  # Loop de Retirada de cédulas
#     if total >= ced:  # //
#         total -= ced  # //
#         totced += 1  # //
#     else:
#         if totced > 0:  # Print da cedula
#             print(f'Você sacou {totced} notas de {ced}')
#         if ced == 50:  # Redução da cédula
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 5
#         elif ced == 5:
#             ced = 2
#         elif ced == 2:
#             ced = 1
#         totced = 0  # !!! Zerar o total de cedulas para o prox loop
#         if total == 0:
#             break  # Saída
# print('Obrigado!')

# 03
# n = int(input('Digite um número inteiro positivo: '))
# mult = 0
# c = 2
# while c < n:
#     if (n % c) == 0:
#         mult += 1
#     c += 1
# if mult == 0:
#     print('Seu número é primo!')
# else:
#     print('Seu número NÃO é primo!')

# 04
n = int(input('Digite um número inteiro positivo: '))
