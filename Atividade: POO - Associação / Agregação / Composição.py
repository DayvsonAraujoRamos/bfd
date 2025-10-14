class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def ler(self):
        print(f"{self.nome} leu o livro {livro.titulo}")  

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
# A pessoa usa o livro,mas nenhum depende da existencia do outro.
pessoa = Pessoa("Maria")    
livro = Livro("Memorias postumas de Bras Cubas")   
pessoa.ler()
# A relaçao acontece quando o metodo ler é executado
# ========================================
class Onibus:
    def __init__(self, linha):
        self.linha = linha
    def embarcar(self, aluno):
        print(f"O {aluno.nome} embarcou no onibus que faz a linha {self.linha} ")

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def pegar_onibus(self, onibus):
        onibus.embarcar(self)

aluno = Aluno("Joao")
onibus = Onibus(4)
aluno.pegar_onibus(onibus)
# ===================================
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def add_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        print(f" Departamento {self.nome}:")
        for x in self.funcionarios:
            print(f" - {x.nome}")

f1 = Funcionario("Pedro")
f2 = Funcionario("Paula")
f3 = Funcionario("Joao")
dep = Departamento("Recursos Humanos")

dep.add_funcionarios(f1)
dep.add_funcionarios(f2)
dep.add_funcionarios(f3)
dep.listar_funcionarios()
# ==========================
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    
    

     
