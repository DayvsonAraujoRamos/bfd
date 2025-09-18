class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self):
        return "bom cliente"
    def 

class Cliente(Usuario):
    ...

pessoa = Cliente("João", "João@gmail.com")
print(pessoa.nome)
print(pessoa.email)
print(pessoa.exibir_informacoes())
