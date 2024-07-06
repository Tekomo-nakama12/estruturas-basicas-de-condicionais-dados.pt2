#operadores relacionais
"""
!=
 >
 <
 >=
 <=
 not
 """
 #operadores logicos
"""
 and &&
 0r||
"""

email_cadastrado = "paula_tejando@gmail.com"
senha_cadastrado = "@bond_cama69"

email_digitado = input("digite seu email: ")
senha_digitado = input('digite sua senha ai : ')

"""
sintaxe criação de uma condicional:
if (condiçção):
    instrução
"""

if (email_cadastrado == email_digitado):
    if (senha_cadastrado== senha_digitado):
        print("acesso permitido")
    else:
        print(" senha invalida ")
else:
    print('email invalido')



"""
if email_cadastrado == email_digitado and senha_cadastrado == senha_digitado:
    print("login feito com sucesso!")
elif email_cadastrado == email_digitado and senha_cadastrado == senha_digitado:
    print("login erro ")
else:
    print("usuario não encontrado")
"""


#outro jeito de fazer concluindo email e senha

email_cadastrado = "paula_tejando@gmail.com"
senha_cadastrado = "@bond_cama69"

email_digitado = input("digite seu email: ")
senha_digitado = input('digite sua senha ai : ')

if (email_cadastrado == email_digitado):
    print('email encontrado com sucesso!')
    senha_digitado = input('digite sua senha ai : ')
    if (senha_cadastrado== senha_digitado):
        print("acesso permitido")
    else:
        print(" senha invalida ")
else:
    print('email invalido')
