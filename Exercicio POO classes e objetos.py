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
# class ContaBancaria:
#     def __init__(self,titular,saldo=0):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self,valor):
#         self.saldo += valor
#         print(f"Foi feito um deposito de {valor} , seu saldo é {self.saldo}")

#     def sacar(self,valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             print(f"Foi feito um saque de {valor} ,seu saldo é {self.saldo}")
#             return True
#         else:
#             print("saldo insuficiente")
#             return False
           
# conta2 = ContaBancaria("Pedro",1000)
# conta3 = ContaBancaria("João,0")
# if conta2.sacar(100):
#     print("Saque realizado com sucesso")
# else:
#     print("Não foi possível efetuar saque")
# ===============================================
# class Aluno:
#     def __init__(self,nome,nota):
#         self.nome = nome
#         self.nota = nota

#     def __str__(self):
#        return f"Aluno: {self.nome}, Nota: {self.nota}"

# aluno5 = Aluno("Maria",9.5)  
# print(aluno5)
# ------------------------------------------------------------------------------------------------
# class Turma:
#     def __init__(self):
#         self.alunos = []
#     def adicionar_aluno(self,aluno):
#        self.alunos.append(aluno)

# aluno1 = Aluno("Pedro",10)
# aluno2 = Aluno("Ana",9)
# aluno3 = Aluno("José",8.5)
# aluno4 = Aluno("Maria",9)

# turma = Turma()
# turma.adicionar_aluno(aluno1)
# turma.adicionar_aluno(aluno2)
# turma.adicionar_aluno(aluno3)
# turma.adicionar_aluno(aluno4)

# for aluno in turma.alunos:
#     print(aluno)
# ============================
class Cachorro:
    especie = "Canis familiaris"
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

cão = Cachorro("toto",4)      
        
print(f"{cão.especie}")
print(f"{Cachorro.especie}")