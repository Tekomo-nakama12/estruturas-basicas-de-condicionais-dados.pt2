
""" codigo para saber se a pessoa ja pode votar, usando condicionais if e else"""


nome = input("Digite o nome da pessoa: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print(f"O cidadão {nome} com {idade} anos está apto a votar")
else:
    print(f"O cidadão {nome} com {idade} anos não está apto a votar")