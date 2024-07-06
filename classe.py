""": = definir um blocos de intrução"""

"""
variavel
nome = 'edinelson' """
"""
função
carac:
1-palavra em python é def
2-tem que ter nome , geralmente auto explicativo
3- é um bloco de codigo que vai manipular algo interno no codigo

1 passo criar
2 chamar  a função
def imprimenome(n):
    retrun  n
"""
"""def imprimenome(nome_usuario ):
    sobrenome ="junior"
    #return luffy5 + sobrenome
    print(nome_usuario + sobrenome)

meu_nome = imprimenome("donatelo_")
print(meu_nome)"""





#formas de chamar uma função

#nome = "gustavo"
#print('gustavo')
#print(nome)
#print (f"o nome é: {nome}")

"""classe é o elemento utilizado para criar objetos
classe -> obj1, obj2,obj3...."""
#atributo = variavel, metodo = função

#classe tbm é nossa forma de bolo
#self= é uma anotação em py, o objeto esta chamando a si msm dentro do codigo


class Pessoa:
    def __init__(self, nome_usuario, idade_usuario, saldo_usuario):
        self.nome = nome_usuario
        self.idade = idade_usuario
        self.saldo = saldo_usuario

obj1 = Pessoa("william", 19, 0)
print(obj1.nome)

obj2 = Pessoa("marcos",23,5)
print(obj2.nome)
         


print('estranho isso né')