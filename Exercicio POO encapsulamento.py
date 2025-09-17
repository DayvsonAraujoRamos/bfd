# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.__saldo = saldo 

#     def __str__(self):
#         return f" Titular: {self.titular} tem {self.__saldo} de saldo"
    
#     def get_saldo(self):
#         return self.__saldo
    
#     def set_saldo(self, novo_saldo):
#         if novo_saldo < 0:
#             print("Saldo não pode ser negativo!")
#         else:
#             self.__saldo = novo_saldo
#             print(f"Seu saldo é R${self.__saldo}")

# pessoa = ContaBancaria("Dayvson", 1000)
# print(pessoa)
# print("Saldo", pessoa.get_saldo())
# pessoa.set_saldo(3500)
# pessoa.set_saldo(-200)
# =============================
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_identidade(self):
        return self.__identidade
    
    def set_identidade(self, nova_identidade):
        self.__identidade = nova_identidade

pessoa = Pessoa("João", "13/04/1991", "34567876401", "124567")

print(pessoa.get_cpf())         
pessoa.set_cpf("65432789065")   
print(pessoa.get_cpf())   
print(pessoa.get_identidade())    
pessoa.set_identidade("345621")  
print(pessoa.get_identidade())
    
        
    
    
    
