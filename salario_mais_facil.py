nome = input('digite o nome do colaborador: ')
salario = float(input("digite o seu salario:"))
novo_salario = 0
if salario <= 1300:
    novo_salario = salario + (salario * (20/100))
elif salario >= 1300.01 and salario <= 2000:
     novo_salario = salario + (salario * (15/100))
elif salario >= 2000.01 and salario <= 3500:
    novo_salario =  novo_salario = salario + (salario * (10/100))
elif salario >= 3500.01 and salario <= 7000:
    novo_salario =  novo_salario = salario + (salario * (5/100))
else:
    novo_salario = salario + (salario * (2/100))
print(f"O colaborador {nome} possui salario atual de  R$ {novo_salario}")

