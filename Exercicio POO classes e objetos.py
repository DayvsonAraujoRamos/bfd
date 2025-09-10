# class Pessoa:
#  def __init__(self,nome,idade):
#   self.nome = nome
#   self.idade = idade
#  def __str__(self):
#   return f" Meu nome é {self.nome} tenho {self.idade} anos"
#  def apresentar(self):
#   print("Olá, meu nome é João e tenho 25 anos.")

# pessoa1 = Pessoa("Dayvson",47)
# pessoa2 = Pessoa( "Marta", 36)
# pessoa1.apresentar()
# ===============================
# class Carro:
#     def __init__(self,marca,modelo,ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def mostrar_informaçoes(self):
#        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\n")

# carro1 = Carro("chevrolet","onix",2020)
# carro2 = Carro("fiat","strada",2023)
# carro3 = Carro("ford","ranger",2025)

# carro1.mostrar_informaçoes()
# carro2.mostrar_informaçoes()
# carro3.mostrar_informaçoes()

# carro1.ano = 2023
# carro1.mostrar_informaçoes()
# ========================================================
class ContaBancaria:
    def __int_(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo
        
        def depositar(self,valor):
            