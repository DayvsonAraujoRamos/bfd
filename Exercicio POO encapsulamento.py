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
    def __init__(self,nome,data_de_nascimento,cpf,identidade):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf
    def get__identidade(self):
        return self.__identidade
    
    
    
   
