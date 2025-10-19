class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    def exibir_informacoes(self):
        return "bom cliente"
    def saudacao(self):
        return "Ola usuario"

class Cliente(Usuario):
    ...
    def __init__(self,nome,email,saldo):
        super().__init__(nome,email)
        self.saldo = saldo
    def __str__(self):
        return f"O seu saldo é {self.saldo}"  
    def saudacao(self):
        return "Ola cliente"
class Funcionario(Cliente):
    ...
class Gerente(Funcionario):
    ...    
    def __str__(self):
        return f" O Gerente {self.nome}, de email {self.email}, tem um saldo de {self.saldo}"

pessoa = Cliente("João", "João@gmail.com","100 reais")
pessoa2 = Gerente("Jose","jose@gmail.com","1000 reais")

print(pessoa.nome)
print(pessoa.email)
print(pessoa.exibir_informacoes())
print(pessoa.saudacao())
print(pessoa.saldo)
print(pessoa)
print(pessoa2)

class Autenticacao:
    def login(self):
        return "Login realizado com sucesso"
    def status(self):
        return "Logado"
class Permissao:
    def verificar_permissao(self):
        return "Permissao verificada com exito"
    def status(self):
        return "Permissao Concedida"
class Administrador(Autenticacao,Permissao):
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

pessoa3 = Administrador("maria","maria@gmail.com")

print(pessoa3.login())
print(pessoa3.verificar_permissao())
#Foi usado o metodo da verificar_permissao() primeira classe herdada
print(Administrador.__mro__)