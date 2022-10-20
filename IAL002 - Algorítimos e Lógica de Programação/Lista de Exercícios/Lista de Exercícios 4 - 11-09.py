# 01
# import random
# lista = random.sample(range(1, 101), 10)
# cont = 0
# maior = 0
# for c in lista:
#     cont += 1
#     if cont == 1:
#         menor = c
#     if c < menor:
#         menor = c
#     if c > maior:
#         maior = c
# print(f'''na lista de números:
#       {lista}
#       o maior é {maior}
#       o menor é {menor}
#     ''')

# 02
# import random
# par = []
# impar = []
# lista = random.sample(range(1, 101), 20)
# for c in lista:
#     if c % 2 == 0:
#         par.append(c)
#     else:
#         impar.append(c)
# print(f'''
#       Da lista {lista}
#       os pares são {par}
#       os ímpares são {impar}''')

# 03
# import random
# vetor1 = random.sample(range(1, 101), 10)
# vetor2 = random.sample(range(1, 101), 10)
# vetor3 = []
# print(vetor1)
# print(vetor2)
# cont = 0
# for c in vetor1:
#     vetor3.insert(cont, c)
#     cont += 2
# cont = 1
# for c in vetor2:
#     vetor3.insert(cont, c)
#     cont += 2
# print(vetor3)

# 04
# import string
# python = []
# texto = '''
# The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone.
# Our community is based on mutual respect, tolerance, and encouragement,
# and we are working to help each other live up to these principles.
# We want our community to be more diverse: whoever you are,
# and whatever your background, we welcome you.
# '''.lower()

# for letra in string.punctuation:
#     texto = texto.replace(letra, ' ')
# lista = texto.split()

# for pal in lista:
#     if pal[0] in 'python':
#         python.append(pal)
#     elif pal[-1] in 'python':
#         python.append(pal)

# print(python)

# 05
# import string
# python = []
# texto = '''
# The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone.
# Our community is based on mutual respect, tolerance, and encouragement,
# and we are working to help each other live up to these principles.
# We want our community to be more diverse: whoever you are,
# and whatever your background, we welcome you.
# '''.lower()

# for letra in string.punctuation:
#     texto = texto.replace(letra, ' ')
# lista = texto.split()

# for pal in lista:
#     if len(pal) > 4:
#         if pal[0] in 'python':
#             python.append(pal)
#         elif pal-1] in 'python':
#             python.append(pal)
# print(python)
