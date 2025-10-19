class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e seu cpf é {self.cpf} "
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, identidade ):
        super().__init__(nome, idade, cpf)
        self.identidade = identidade
    def __str__(self):
        return f"O funcionário {self.nome} tem {self.idade} anos, seu cpf é {self.cpf} e sua idantidade é {self.identidade} "   
    
pessoa1 = Pessoa("Dayvson", 27, "988977999-55")
pessoa2 = Funcionario("João", 34, "123324654-83", 555555 )

print(pessoa1)
print(pessoa2)
