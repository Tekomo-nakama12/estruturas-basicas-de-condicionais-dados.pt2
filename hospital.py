###hospital

nome = input("Digite o nome do paciente: ")
idade = int(input('Digite a idade do paciente: '))
peso = float(input('Digiteo peso do paciente: '))
altura = float(input("digite a altura do paciente: "))
sintoma = input('digite o sintoma do paciente:')
print(f'O PACIENTE DE NOME {nome}, E IDADE DE APROXIMADAENTE {idade}, E DE PESO {peso}, e de uma altura em metros de {altura}, chegou ao hospital com sintomas de {sintoma}')




##impar ou par 

numero = int(input('digite um numero: ')) 
if numero %2==0:
    print(f"o numero {numero} FINO SENÕRES é par  ")

else:
 print(f"O numero {numero} é impar SENÕRES ")